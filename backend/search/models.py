# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class SiteCategory(models.Model):
    """Тематика сайта"""
    category = models.TextField(verbose_name='Domain URL', blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.category}'
    
    class Meta:
        db_table = "search_site_categories"
        ordering = ['category']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Site(models.Model):
    """Домены сайтов. Для будущей аналитики и другого функционала будем сохранять все известные нам доменые имена"""
    url = models.TextField(verbose_name='URL сайта', blank=False, null=False, unique=True)
    category = models.ForeignKey(SiteCategory, verbose_name='Категория сайта', on_delete=models.SET_NULL, blank=True, null=True)
    integration_hash = models.TextField(verbose_name='Хэш для интеграции метрики', blank=False, null=False, unique=True)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)

    def __str__(self):
        return f'{self.url}'
    
    class Meta:
        db_table = "search_sites"
        ordering = ['url']
        verbose_name = 'Сайт'
        verbose_name_plural = 'Все известные сайты'


class Word(models.Model):
    """Все известные слова (используются для полнотекстового поиска)"""
    word = models.TextField(verbose_name='Word', blank=False, null=False, unique=True)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)

    def search_in_pages(self):
        # TODO: напиши здесь поиск новых слов
        
        pass

    def __str__(self):
        return f'Слово #{self.id}:{self.word}'

    class Meta:
        db_table = "search_words"
        ordering = ['word']
        verbose_name = 'Слово'
        verbose_name_plural = 'Слова'


class Page(models.Model):
    """Основная информация о страничке"""
    site = models.ForeignKey(Site, verbose_name='Сайт страницы', on_delete=models.CASCADE, blank=False, null=False)
    url = models.TextField(verbose_name='URL', blank=False, null=False, unique=True)
    title = models.TextField(verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    keywords = models.TextField(verbose_name='Ключевые слова')
    status_code = models.IntegerField(verbose_name='Status Code', default=500)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)
    updated = models.DateTimeField(verbose_name='Запись обновлена', default=timezone.now)

    def __str__(self):
        return f'Страница #{self.id}:{self.title[:25]}'

    class Meta:
        db_table = "search_pages"
        ordering = ['url']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class WordsInPages(models.Model):
    """Какие слова есть на страницах (нужно для полнотекстового поиска)"""
    words = ArrayField(ArrayField(models.IntegerField()))
    page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)
    # TODO: как быть с переиндексацией страниц?

    def __str__(self):
        return f'Слова страницы #{self.page.id}:{self.page.title[:25]}'

    class Meta:
        db_table = "search_words_in_pages"
        ordering = ['page']
        verbose_name = 'Слова на странице'
        verbose_name_plural = 'Слова на страницах'


class Link(models.Model):
    """Все известные ссылки. Используется сетевыми краулерами для обхода страниц"""
    url = models.TextField(verbose_name='URL', blank=False, null=False, unique=True)
    text = models.TextField(verbose_name='Текст ссылки', blank=False, null=False)
    page = models.TextField(verbose_name='Страница, на которой ссылка была встречена', blank=False, null=False)
    visited = models.BooleanField(verbose_name='Посещалась', default=False)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)
    spyder_name = models.TextField(verbose_name='Имя паука', default='spyder_1')
    debug = models.TextField(verbose_name='Ссылка в изначальном виде', blank=True, null=True)  # TODO: отладочное поле. Удалить

    # TODO: создать уникальную связку. Позволять дублирование. Или нет?
    # многие сайты могут ссылаться на один ресурс, это позволит эффективно находить ресурс по тексту ссылки
    # но это не означает, что страницу нужно каждый раз посещать
    # думаю стоит разрешить дублирование, но перед посещением проверять посещалась ли страница последние N дней

    def __str__(self):
        return f'Ссылка #{self.id}:{self.text[:25]}'
    
    class Meta:
        db_table = "search_links"
        ordering = ['url']
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'


class SitesQueue(models.Model):
    """
    Очередь на индексацию. Для ручного добавления сайтов на индексацию пользователями. 
    Данная очередь имеет для краулера больший приоритет перед другими ссылками.

    По сути краулер должен извлекать из этой таблицы URL нового сайта и ставить пометку visited.
    Дальнейшая работа со ссылками данного сайта происходит в модели Link
    """
    url = models.TextField(verbose_name='Domain URL', blank=False, null=False, unique=True)
    visited = models.BooleanField(verbose_name='Посещался', default=False)
    spyder_name = models.TextField(verbose_name='Имя паука', blank=True, null=True, default=None)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)

    def __str__(self):
        return f'Домен #{self.id}:{self.url}'
    
    class Meta:
        db_table = "search_sites_queue"
        ordering = ['url']
        verbose_name = 'Домен'
        verbose_name_plural = 'Очередь на индексацию'


class SearchQuery(models.Model):
    """
    Уникальные поисковые запросы. 
    Для каждого запроса можно создать связку с определенной страницей. Эта страница всегда будет первой в выдаче
    """
    query = models.TextField(verbose_name='Search query', blank=False, null=False, unique=True)
    page = models.ForeignKey(Page, verbose_name='Страница', on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)
    # TODO: возможно стоит создать таблицу, учитывающую популярность поисковых запросов для аналитики. Но пока это не нужно

    def __str__(self):
        return f'Поисковой запрос #{self.id}:{self.query}'
    
    class Meta:
        db_table = "search_query"
        ordering = ['query']
        verbose_name = 'Поисковой запрос'
        verbose_name_plural = 'Поисковые запросы'


class Metrics(models.Model):
    """Информация о том, как долго пользователь находится на странице сайта"""
    site = models.ForeignKey(Site, verbose_name='Сайт страницы', on_delete=models.CASCADE, blank=False, null=False)
    user_hash = models.TextField(verbose_name='Хэш пользователя')
    created = models.DateTimeField(verbose_name='Запись создана', default=timezone.now)
    updated = models.DateTimeField(verbose_name='Запись обновлена', default=timezone.now)

    def __str__(self):
        return f'Данные метрики #{self.id}: {self.user_hash} {self.site} '
    
    class Meta:
        db_table = "search_metric"
        ordering = ['site']
        verbose_name = 'Метрика сайта'
        verbose_name_plural = 'Метрики сайтов'
