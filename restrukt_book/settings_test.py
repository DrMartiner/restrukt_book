# -*- coding: utf-8 -*-

from settings import *

SECRET_KEY = 'asdsfgdfsdfgsd'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

EMAIL_BACKEND = 'eml_email_backend.EmailBackend'
EMAIL_FILE_PATH = 'media/emails/'

SOUTH_TESTS_MIGRATE = False
SKIP_SOUTH_TESTS = True