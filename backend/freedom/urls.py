# -*- coding: utf-8 -*-
"""Search machine URL endpoints"""
from django.contrib import admin
from django.urls import path

from freedom import settings
from search.views import Statistics, StartedQuery, Search, RegisterSite


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Statistics.as_view(), name='statistics'),
    path('started_query', StartedQuery.as_view(), name='started_query'),
    path('search', Search.as_view(), name='search'),
    path('register_site', RegisterSite.as_view(), name='register_site'),
]
