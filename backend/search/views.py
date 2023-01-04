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

    def get(request) -> JsonResponse:
        """Отвечает за ебучий поиск"""
        search_query = ''.split()
        pages = []
        for word in search_query:
            pass
