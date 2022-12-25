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


class Weather(View):
    """Json template for debug"""

    @staticmethod
    def get(request) -> JsonResponse:
        """get json-responseg"""
        return JsonResponse({
            "id": 1,
            "location": "London",
            "abbr": "s",
            "time": "07:15 pm",
            "temp": 59
          }, status=200)

class Search(View):
    """Отвечает за ебучий поиск"""

    def get(request) -> JsonResponse:
        search_query = ''.split()
        pages = []
        for word in search_query:
            pass
