# -*- coding: utf-8 -*-
"""Search machine URL endpoints"""
from django.contrib import admin
from django.urls import path

from freedom import settings
from search.views import Statistics, Search


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Statistics.as_view(), name='statistics'),
    path('search', Search.as_view(), name='search'),
]
