# coding: utf-8

from decouple import config

WTF_CSRF_ENABLED = True
SECRET_KEY = config('SECRET_KEY', default='')
CSRF_ENABLED = True
DEBUG = config('DEBUG', default=False, cast=bool)

LANGUAGES = {
    'en': 'English',
    'pt': 'Português'
}
