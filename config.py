# coding: utf-8

import os
from decouple import config

BASEDIR = os.path.abspath(os.path.dirname(__file__))
WTF_CSRF_ENABLED = True
SECRET_KEY = config('SECRET_KEY', default='')
CSRF_ENABLED = True
DEBUG = config('DEBUG', default=False, cast=bool)
TITLE = 'CSS Simple Tools'
LANGUAGES = {
    'en': 'English',
    'pt': 'Português'
}
