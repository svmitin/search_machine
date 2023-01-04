# -*- coding: utf-8 -*-
"""Internet spyder bot"""
import sys
import requests
from requests.exceptions import ConnectionError, MissingSchema, InvalidSchema
from urllib.parse import urlparse

import click
from bs4 import BeautifulSoup
from datetime import datetime
from sqlalchemy.exc import IntegrityError, PendingRollbackError
from psycopg2.errors import UniqueViolation

from dbase import DBSession
from dbase import Word, Page, WordsInPages, Link
from constants import *
from helpers import validate_word


class Spyder:
    name = ''

    def __init__(self, name: str):
        self.name = name

    def normalyze_link(self, link: str, parent: str) -> str or None:
        """Получает URL ссылки, URL её владельца, возвращает нормализованную глобальную ссылку"""
        if not link or not parent:
            return None
        
        link = link.lower().lstrip('//')
        
        # игнорируем мусор
        block_starts = ['tel:', 'mailto:', 'skype:', 'magnet:', 'tg:', '#']
        for startswith in block_starts:
            if link.startswith(startswith):
                return None

        # TODO: здесь мы генерируем ошибку. Нужна отладка
        scheme, domain = urlparse(link).scheme, urlparse(link).netloc
        if not scheme or not domain:
            # на случай не полной ссылки вроде /about и т.п.
            link = f'{urlparse(parent).scheme}://{urlparse(parent).netloc}/{link.lstrip("/")}'
        
        # Проверка доменной зоны. Ходим только в .RU
        try:
            zone = urlparse(link).netloc.split('.')[-1]
        except KeyError:
            return None
        if zone not in ACCEPTED_ZONES:
            return None

        # Домен не должен быть включен в черный список
        if urlparse(link).netloc in DOMAIN_BLACKLIST:
            return None
        return link

    def link_type(self, link: str) -> str:
        link = link.partition('?')
        
        for extesion in PAGE_EXTENSIONS:
            if link.endswith(extesion):
                return 'page'
        
        for extesion in PICTURES_EXTENSIONS:
            if link.endswith(extesion):
                return 'picture'
        
        for extesion in DOCUMENT_EXTENSIONS:
            if link.endswith(extesion):
                return 'document'
        
        for extesion in SOUND_EXTENSIONS:
            if link.endswith(extesion):
                return 'sound'
        
        for extesion in IMAGES_EXTENSIONS:
            if link.endswith(extesion):
                return 'image'  # .iso
        
        return 'page'

    def open_new_url(self) -> Link or None:
        link = DBSession.query(Link).filter_by(
            visited=False,
            spyder_name=self.name
        ).first()

        if not link:
            return None
        
        link.visited = True
        link.save()
        return link

    def get_page_title(self, page_html: str) -> str:
        """Parse page, search description"""
        try:
            soup = BeautifulSoup(page_html, 'html.parser')
            return soup.title.string
        except (TypeError, TypeError, KeyError, AttributeError):
            return ''
    
    def get_page_description(self, page_html: str) -> str:
        """Parse page, search description"""
        try:
            soup = BeautifulSoup(page_html, 'html.parser')
            return soup.find("meta", attrs={"name": "description"})['content']
        except (TypeError, TypeError, KeyError, AttributeError):
            return ''

    def get_page_keywords(self, page_html: str) -> str:
        """Parse page, search description"""
        try:
            soup = BeautifulSoup(page_html, 'html.parser')
            return soup.find("meta", attrs={"name": "keywords"})['content']
        except (TypeError, TypeError, KeyError, AttributeError):
            return ''

    def get_page_text(self, page_html: str) -> str:
        """Parse page, search text"""
        try:
            soup = BeautifulSoup(page_html, 'html.parser')
            page_text = ''
            divs = soup.find_all('div')
            for div in divs:
                page_text += div.get_text()
            return page_text
        except (TypeError, TypeError, AttributeError):
            return ''

    def make_page_index(self, page: Page, page_content: str) -> None:
        """Indexing all words in page"""
        # конкатенируем все слова страницы, валидируем символы, преобразуем в список
        all_page_text = f'{page.title} {page.description} {page.keywords} {page_content}'.lower()
        for symbol in PUNCTUATION_SYMBOLS:
            all_page_text = all_page_text.replace(symbol, '')
        all_page_words = all_page_text.split()
        words = filter(validate_word, set(all_page_words))
        words_ids = []

        # пробегаемся по словам страницы. Если слово уже известно поисковой системе, добавляем страницу в индекс
        # если нет - регистрируем слово и добавляем страницу в индекс
        for word in words:
            saved_word = DBSession.query(Word).filter_by(word=word).first()
            if not saved_word:
                saved_word = Word(word=word)
                saved_word.add()
            words_ids.append(saved_word.id)

        # добавляем страницу в индекс
        index = WordsInPages(words=words_ids, page_id=page.id)
        index.add()

    def parse_page(self, url: str) -> None:
        try:
            response = requests.get(url)
            status_code = response.status_code
            print(f'Get page: {status_code} {url}')
            title=self.get_page_title(page_html=response.text)
            description=self.get_page_description(page_html=response.text)
            keywords=self.get_page_keywords(page_html=response.text)
        except (ConnectionError, MissingSchema, InvalidSchema) as error:
            print(f'ERROR: {error}')
            return None
        
        if not title and not description and not keywords:
            print('not title or not description or not keywords')
            return None

        # Сохранение базовой информации о странице: URL, описание, ключевые слова
        soup = BeautifulSoup(response.text, 'html.parser')
        page = Page(url=url,
                    title=self.get_page_title(page_html=response.text),
                    description=self.get_page_description(page_html=response.text),
                    keywords=self.get_page_keywords(page_html=response.text),
                    status_code=status_code,
                    created=datetime.utcnow().isoformat(),
                    updated=datetime.utcnow().isoformat())
        page.add()
        
        # Создание индекса страницы
        self.make_page_index(
            page=page, 
            page_content=self.get_page_text(page_html=response.text)
        )

        # save page links
        for a in soup.find_all('a'):
            url = self.normalyze_link(link=a.get('href'), parent=page.url)
            if not url:
                continue
            link = Link(url=url,
                        text=a.text.strip(),
                        page=self.normalyze_link(link=page.url, parent=page.url),
                        created=datetime.utcnow().isoformat(),
                        spyder_name=self.name,
                        debug=a.get('href') # сохраняем в дебаг ссылку в инзначальном виде
            )
            link.add()

    def start(self, start_url: str):
        link = Link(url=start_url) if start_url else self.open_new_url()
        while link:
            self.parse_page(url=link.url)
            link = self.open_new_url()
        print('Очередь URL пуста')

@click.command()
@click.option('--start_url', default=None, help='Page URL for start work')
@click.option('--spyder_name', default='spyder_1', help='Name for spyder')
def run(start_url, spyder_name):
    spyder = Spyder(name=spyder_name)
    spyder.start(start_url=start_url)


if __name__ == '__main__':
    run()
