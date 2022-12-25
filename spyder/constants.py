# -*- coding: utf-8 -*-
import os

DB_HOST = os.environ.get('FREEDOM_DB_HOST')
DB_NAME = os.environ.get('FREEDOM_DB_NAME')
DB_USER = os.environ.get('FREEDOM_DB_USER')
DB_PASS = os.environ.get('FREEDOM_DB_PASS')
DB_PORT = os.environ.get('FREEDOM_DB_PORT')

ACCEPTED_ZONES = ('ru',)
DOMAIN_BLACKLIST = ('google.com', 'google.ru', 'vk.com', 'mail.ru', 'yandex.com', 'facebook.com', 'twitter.com', 'telegram.com', 'mail.ru', 'ok.ru', 'dzen.ru')

ACCEPTED_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
PUNCTUATION_SYMBOLS = ',.?!:;\'"`'
WORDS_BLACKLIST = ('пиздарог',) # и другие выдуманные слова

PAGE_EXTENSIONS = ('.htm', '.html', '.xhtml', '.php')     # AND OTHERS!
PICTURES_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')
DOCUMENT_EXTENSIONS = ('.doc', '.docx', '.xlsx', '.pdf', '.epub', '.fb2')
SOUND_EXTENSIONS = ('.mp3', '.wav', '.ogg', '.flac')
IMAGES_EXTENSIONS = ('.iso')
