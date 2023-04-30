# -*- coding: utf-8 -*-
import os

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = int(os.environ.get('DB_PORT'))

ACCEPTED_ZONES = ('ru', 'org', 'com', 'net',)
DOMAIN_BLACKLIST = ('google.com', 'google.ru', 'vk.com', 'yandex.com', 'facebook.com', 'twitter.com', 'telegram.com', 'ok.ru',)

ACCEPTED_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz1234567890'
PUNCTUATION_SYMBOLS = ',.?!:;\'"`'
WORDS_BLACKLIST = ('пиздарог',) # и другие выдуманные слова

PAGE_EXTENSIONS = ('.htm', '.html', '.xhtml', '.php')     # AND OTHERS!
PICTURES_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')
DOCUMENT_EXTENSIONS = ('.doc', '.docx', '.xlsx', '.pdf', '.epub', '.fb2')
SOUND_EXTENSIONS = ('.mp3', '.wav', '.ogg', '.flac')
IMAGES_EXTENSIONS = ('.iso')
