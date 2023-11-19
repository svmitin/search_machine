import os


DEBUG = bool(os.environ.get('DEBUG')) or False

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_PORT = int(os.environ.get('DB_PORT'))

ACCEPTED_SYMBOLS = 'abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюяё '