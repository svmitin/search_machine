"""i2p crawler bot"""
import random
import requests
from requests.exceptions import ConnectionError, MissingSchema, InvalidSchema
from urllib.parse import urlparse
import hashlib

import click
from bs4 import BeautifulSoup
from datetime import datetime

from dbase import DBSession
from dbase import Word, Page, WordsInPages, Link, Site, SitesQueue
from constants import *
from helpers import in_blacklist, validate_word


class Crawler:
    candidates = None

    def __init__(self):
        self.candidates = []

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
            link = f'http://{urlparse(parent).netloc}/{link.lstrip("/")}'
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
        if not self.candidates:
            # новые. Первичная индексация. Достаем 100 самых старых
            links_for_index = DBSession.query(
                Link
            ).filter_by(
                Link.visited.is_(False)
            ).order_by(
                Link.created.desc()
            ).all()[100]

            # Посещенные. Повторная индексация. Достаем 100 самых старых
            pages_urls_for_reindex = [row.url for row in DBSession.query(
                Page
            ).order_by(
                Page.updated.desc()
            ).all()[100]]

            links_for_reindex = DBSession.query(
                Link
            ).filter_by(
                Link.visited.is_(True),
                Link.url.in_(pages_urls_for_reindex)
            ).order_by(
                Link.created.desc()
            ).all()[100]

            self.candidates = [] + links_for_index + links_for_reindex

        link = random.choice(self.candidates)
        if not link:
            return
        
        link.visited = True
        link.save()
        return link

    def get_page_title(self, page_html: str) -> str:
        """Parse page, search title"""
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
        """Parse page, search keywords"""
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
                page_text += f'{div.get_text(sep=" ")} '
            return page_text
        except (TypeError, TypeError, AttributeError):
            return ''

    def make_page_index(self, page: Page, page_content: str) -> None:
        """Индексируем все слова на странице. Нужно для полнотекстового поиска"""
        # конкатенируем все слова страницы, валидируем символы, преобразуем в список
        all_page_text = f'{page.title} {page.description} {page.keywords} {page_content}'.lower()
        for symbol in PUNCTUATION_SYMBOLS:
            all_page_text = all_page_text.replace(symbol, ' ')
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
            response = requests.get(url, proxies={'http': 'socks5h://127.0.0.1:4447'})
            status_code = response.status_code
            print(f'Get page: {datetime.now().strftime("%H:%M:%S")} {status_code} {url}')
            title=self.get_page_title(page_html=response.text)
            description=self.get_page_description(page_html=response.text)
            keywords=self.get_page_keywords(page_html=response.text)
        except (ConnectionError, MissingSchema, InvalidSchema) as error:
            print(f'ERROR: {error}')
            return

        if not title and not description and not keywords:
            print('not title or not description or not keywords')
            return

        # сохраняем домен как сайт
        domain_url = f'{urlparse(url).scheme}://{urlparse(url).netloc}'
        site = DBSession.query(Site).filter_by(url=domain_url).first()
        if not site:
            hash = hashlib.sha3_256(f'{domain_url}{str(datetime.now())}'.encode('utf-8')).hexdigest()
            site = Site(url = domain_url, integration_hash = hash)
            site.add()

        # сохранение базовой информации о странице: URL, описание, ключевые слова
        soup = BeautifulSoup(response.text, 'html.parser')
        page = Page(
            url=url,
            site_id=site.id,
            title=self.get_page_title(page_html=response.text),
            description=self.get_page_description(page_html=response.text),
            keywords=self.get_page_keywords(page_html=response.text),
            status_code=status_code,
            created=datetime.utcnow().isoformat(),
            updated=datetime.utcnow().isoformat()
        )
        page.add()

        # создание индекса страницы
        self.make_page_index(
            page=page, 
            page_content=self.get_page_text(page_html=response.text)
        )

        # сохраняем ссылки страницы
        for a in soup.find_all('a'):
            url = self.normalyze_link(link=a.get('href'), parent=page.url)
            if not url:
                continue
            link = Link(url=url,
                        text=a.text.strip().lower(),
                        page=self.normalyze_link(link=page.url, parent=page.url),
                        created=datetime.utcnow().isoformat(),
                        debug=a.get('href') # сохраняем в дебаг ссылку в изначальном виде
            )
            link.add()

    def start(self, start_url: str):
        link = Link(url=start_url) if start_url else self.open_new_url()
        while link:
            save = True

            url = link.url
            print(f'url: {url}')
            # Проверка доменной зоны. Ходим только в .RU
            try:
                zone = urlparse(url).netloc.split('.')[-1]
            except KeyError:
                save = False
            if zone not in ACCEPTED_ZONES:
                save = False

            # Домен не должен быть включен в черный список
            if in_blacklist(url):
                save = False

            if save:
                self.parse_page(url=url)

            link = self.open_new_url()
            if not link:
                break
        print('Очередь URL пуста')

@click.command()
@click.option('--start_url', default=None, help='Page URL for start work')
def run(start_url):
    crawler = Crawler()
    crawler.start(start_url=start_url)
    # перезапуск краулера с сайтом, в ручную добавленным на индексацию
    while True:
        site = DBSession.query(SitesQueue).filter_by(visited=False).first()
        if not site:
            return
        site.visited = True
        site.save()
        crawler.start(start_url=site.url)


if __name__ == '__main__':
    run()
