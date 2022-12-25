# -*- coding: utf-8 -*-
from constants import *


def validate_word(word: str):
    # в слово могут попасть знаки препинания
    for symbol in PUNCTUATION_SYMBOLS:
        word = word.replace(symbol, '')

    if len(word) < 3:           # сразу нахуй
        return False
    
    if word.startswith('#'):    # это тэг, а не слово
        return False

    if word.startswith('@'):    # вероятно это обращение
        return False

    cleared = ''
    for symbol in word:
        if symbol in ACCEPTED_SYMBOLS:
            cleared += symbol
    if len(cleared) == len(word) and word not in WORDS_BLACKLIST:
        return True
    return False
