# -*- coding: utf-8 -*-

import sys
import os.path
from os import path
import dj_database_url

try:
    from settings_local import *
except ImportError:
    print "Don't forget create settings_local.py"

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

SITE_NAME = path.basename(path.realpath(path.curdir))
SITE_ROOT = os.path.join(path.realpath(path.pardir), SITE_NAME)

DEBUG = bool(os.environ.get('DEBUG', False))
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Alexey Kuzmin', 'DrMaritner@gmail.com'),
)
MANAGERS = ADMINS

ADMIN_HONEYPOT_EMAIL_ADMINS = False

DATABASE_URL_DEFAUL = os.environ.get('DATABASE_URL_DEFAUL')
if DATABASE_URL_DEFAUL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL_DEFAUL),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'database.sqlite3',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        },
    }

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'local.drmartiner.pro',
]
INTERNAL_IPS = ALLOWED_HOSTS

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))
COMPRESS_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = os.environ['SECRET_KEY']

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
if not DEBUG:
    TEMPLATE_LOADERS += ('django.template.loaders.eggs.Loader', )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'constance.context_processors.config',
)

ROOT_URLCONF = SITE_NAME + '.urls'
WSGI_APPLICATION = SITE_NAME + '.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',

    'admin_honeypot',
    'constance',
    'south',
    'email_html',
    'djangojs',
    'compressor',

    'apps.simple_page',

    'django_cleanup',

    'django_coverage',
    'django_factory_boy',
)

CONSTANCE_BACKEND = 'constance.backends.redisd.RedisBackend'
CONSTANCE_SUPERUSER_ONLY = True
CONSTANCE_REDIS_CONNECTION = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
}
CONSTANCE_CONFIG = {
    'SITE_TITLE': (u'Книга Реструкт', 'Title'),
    'SITE_KEYWORDS': (u' ', 'keywords'),
    'SITE_DESCRIPTION': (u' ', 'description'),
    'SITE_404_TITLE': (u' ', u'Заголовок 404'),
    'SITE_404_TEXT': (u' ', u'Текст 404'),
    'SITE_500_TITLE': (u' ', u'Заголовок 500'),
    'SITE_500_TEXT': (u' ', u'Текст 500'),
    'ORDER_SUCCESS_TITLE': (u' ', u'Заголовок успешной оплаты'),
    'ORDER_SUCCESS_TEXT': (u' ', u'Текст успешной оплаты'),
    'ORDER_FAIL_TITLE': (u' ', u'Заголовок неуспешной оплаты'),
    'ORDER_FAIL_TEXT': (u' ', u'Текст неуспешной оплаты'),
}

LOGGING_DIR = os.path.join(SITE_ROOT, 'logs')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'message': {
            'format': '(%(asctime)s) %(name)s - %(levelname)s: [%(filename)s %(funcName)s %(lineno)d]: %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'messages.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'message',
        },
        'request_handler': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'request.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'message',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default',],
            'level': 'ERROR',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler', ],
            'level': 'ERROR',
            'propagate': False
        },
        'messages': {
            'handlers': ['default', ],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

try:
    from settings_local import *
except ImportError:
    pass