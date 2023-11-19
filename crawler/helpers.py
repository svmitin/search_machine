from constants import *


def in_blacklist(url):
    for domain in DOMAIN_BLACKLIST:
        if domain in url:
            return True
    return False


def validate_word(word: str) -> bool:
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
