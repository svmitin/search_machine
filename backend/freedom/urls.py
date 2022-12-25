# -*- coding: utf-8 -*-
"""Search machine URL endpoints"""
from django.contrib import admin
from django.urls import path

from freedom import settings
from search.views import Weather


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Weather.as_view(), name='root'),
    path('weather.json', Weather.as_view(), name='main'),
]
