"""Search machine URL endpoints"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import static

from freedom import settings
from search.views import MainPage
from search.views import Statistics, Search


admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('search', Search.as_view(), name='search'),
    path('statistics', Statistics.as_view(), name='statistics'),
]
