# -*- coding: utf-8 -*-
"""Core application admin module."""
from django.contrib import admin
from django.utils.html import mark_safe

from search.models import Word, Page, WordsInPages, Link, Domain, DomainsQueue, SearchQuery


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


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """Admin class for Domain model."""
    list_display = ('id', 'url', 'created',)
    list_display_links = ('id', 'url',)
    search_fields = ('url',)
    ordering = ('-id',)


@admin.register(DomainsQueue)
class DomainsQueueAdmin(admin.ModelAdmin):
    """Admin class for DomainsQueue model."""
    list_display = ('id', 'url', 'visited', 'spyder_name', 'created',)
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
