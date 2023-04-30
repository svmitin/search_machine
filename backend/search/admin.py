# -*- coding: utf-8 -*-
"""Core application admin module."""
from django.contrib import admin
from django.utils.html import mark_safe

from search.models import SiteCategory, Site, Word, Page, WordsInPages, Link, SitesQueue, SearchQuery


@admin.register(SiteCategory)
class SiteCategoryAdmin(admin.ModelAdmin):
    """Admin class for SiteCategory model."""
    list_display = ('id', 'category',)
    list_display_links = ('id', 'category',)
    search_fields = ('category',)
    ordering = ('-id',)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    """Admin class for Site model."""
    list_display = ('id', 'url', 'category', 'created',)
    list_display_links = ('id', 'url',)
    search_fields = ('url',)
    ordering = ('-id',)


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin class for Word model."""
    list_display = ('id', 'word', 'created',)
    list_display_links = ('id', 'word',)
    search_fields = ('id', 'word', 'created',)
    ordering = ('-id', 'word',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Admin class for Page model."""
    list_display = ('id', 'url', 'title', 'status_code', 'created', 'updated',)
    list_display_links = ('id', 'url',)
    search_fields = ('url', 'title', 'description', 'keywords',)
    ordering = ('-id', 'url',)


@admin.register(WordsInPages)
class WordsInPagesAdmin(admin.ModelAdmin):
    """Admin class for WordsInPages model."""
    list_display = ('id', 'page', 'created',)
    list_display_links = ('id', 'page',)
    search_fields = ('url', 'page',)
    ordering = ('-id', 'page',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """Admin class for Link model."""
    list_display = ('id', 'url', 'text', 'page', 'visited', 'created',)
    list_display_links = ('id', 'url',)
    search_fields = ('url', 'text', 'page',)
    ordering = ('-id', 'url', 'page', 'visited',)


@admin.register(SitesQueue)
class SitesQueueAdmin(admin.ModelAdmin):
    """Admin class for SitesQueue model."""
    list_display = ('id', 'url', 'visited', 'crawler_name', 'created',)
    list_display_links = ('id', 'url',)
    search_fields = ('url',)
    ordering = ('-id',)


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    """Admin class for SearchQuery model."""
    list_display = ('id', 'query', 'page', 'created',)
    list_display_links = ('id', 'query',)
    search_fields = ('query',)
    ordering = ('-id',)
