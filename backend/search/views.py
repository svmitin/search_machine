from freedom.settings import DEBUG
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.utils.timezone import timedelta
from django.core.validators import validate_email, ValidationError
from django.core.paginator import Paginator
from django.db import connection
from django.db.models import Max

from .models import Word, Page, WordsInPages, Link


class Statistics(View):

    @staticmethod
    def get(request) -> JsonResponse:
        """Возвращает статистику"""
        return JsonResponse({
            'Words': Word.objects.count(),
            'Pages': Page.objects.count(),
            'WordsInPages': WordsInPages.objects.count(),
            'Links': Link.objects.count()
          }, status=200)

class Search(View):

    @staticmethod
    def get(request) -> JsonResponse:
        """Отвечает за ебучий поиск"""

        # полнотекстовый поиск
        # 1) разбиваем текстовый запрос на отдельные слова
        # 2) находим id каждого слова
        # 3) извлекаем из WordsInPages все страницы на которых есть все эти слова
        # 4) извлекаем из Page информацию о данных страницах для возврата пользователю
        search_query = request.GET.get('query', '').split()
        words_ids = []
        for word in search_query:
            word = Word.objects.filter(word=word.lower()).first()
            if not word:
                continue
            words_ids.append(word.id)
        
        if not words_ids:
            return JsonResponse({'pages': []}, status=200)
        
        found_pages = WordsInPages.objects.filter(words__contains=[words_ids]).all()
        return JsonResponse({
            'pages': [
                {
                    'url': found_page.page.url,
                    'title': found_page.page.title,
                    'description': found_page.page.description,
                } for found_page in found_pages
            ]
        }, status=200)
