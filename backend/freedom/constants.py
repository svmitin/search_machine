# -*- coding: utf-8 -*-
import os


DEBUG = bool(os.environ.get('FREEDOM_DEBUG')) or False

DB_HOST = os.environ.get('FREEDOM_DB_HOST')
DB_NAME = os.environ.get('FREEDOM_DB_NAME')
DB_USER = os.environ.get('FREEDOM_DB_USER')
DB_PASS = os.environ.get('FREEDOM_DB_PASS')
DB_PORT = os.environ.get('FREEDOM_DB_PORT')

ACCEPTED_SYMBOLS = 'abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюяё '