from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import timedelta
from django.core.validators import validate_email, ValidationError
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Max

from freedom.settings import DEBUG
from .models import Word, Page, WordsInPages, Link, Domain, SearchQuery


class Statistics(View):

    @staticmethod
    def get(request) -> JsonResponse:
        """Возвращает статистику"""
        return JsonResponse({
            'Words': Word.objects.count(),
            'Pages': Page.objects.count(),
            'WordsInPages': WordsInPages.objects.count(),
            'Links': Link.objects.count(),
            'Domain': Domain.objects.count(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
          }, status=200)

class Search(View):

    @staticmethod
    def ready_answer_search(query: str) -> list:
        """Возвращает уже готовый ответ (если таковой уже был добавлен человеком)"""
        search_query = SearchQuery.objects.filter(query=query, page__isnull=False).order_by('-created').all()[:2]
        return [
            {
                'url': found_page.page.url,
                'title': found_page.page.title,
                'description': found_page.page.description,
                'indexed': found_page.page.created,
                'found_with': 'ready answer search'
            } for found_page in search_query
        ]

    @staticmethod
    def links_search(query: str) -> list:
        """Поиск по тексту ссылок"""
        links = [link.url for link in Link.objects.filter(text=query).all()]
        found_pages = Page.objects.filter(url__in=links).all()
        return [
            {
                'url': found_page.url,
                'title': found_page.title,
                'description': found_page.description,
                'indexed': found_page.created,
                'found_with': 'links search'
            } for found_page in found_pages
        ]

    @staticmethod
    def full_text_search(query: str) -> list:
        """Полнотекстовый поиск"""
        # 1) разбиваем текстовый запрос на отдельные слова
        # 2) находим id каждого слова
        # 3) извлекаем из WordsInPages все страницы на которых есть все эти слова
        # 4) извлекаем из Page информацию о данных страницах для возврата пользователю
        query = query.split()
        words_ids = []
        for word in query:
            word = Word.objects.filter(word=word.lower()).first()
            if not word:
                continue
            words_ids.append(word.id)
        
        if not words_ids:
            return []
        
        found_pages = WordsInPages.objects.filter(words__contains=[words_ids]).order_by('-created').all()[:100]
        return [
            {
                'url': found_page.page.url,
                'title': found_page.page.title,
                'description': found_page.page.description,
                'indexed': found_page.page.created,
                'found_with': 'full text search'
            } for found_page in found_pages
        ]

    @staticmethod
    def get(request) -> JsonResponse:
        """Отвечает за поиск"""
        query = request.GET.get('query', '').lower().strip()

        # сохраним запрос в историю
        search_query = SearchQuery.objects.filter(query=query).first()
        if not search_query:
            search_query = SearchQuery(query=query)
            search_query.save()

        ready_answer_search_results = Search.ready_answer_search(query = query)
        links_search_results = Search.links_search(query = query)
        full_text_search_results = Search.full_text_search(query = query)

        result = [
            *ready_answer_search_results,
            *links_search_results,
            *full_text_search_results
        ]

        return JsonResponse({
            'pages': result
        }, status=200)
