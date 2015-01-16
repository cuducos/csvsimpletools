# coding: utf-8

import os
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY', default='')

BASEDIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
WTF_CSRF_ENABLED = True

TITLE = 'CSV Simple Tools'
LANGUAGES = {
    'en': 'English',
    'pt': 'Português'
}
