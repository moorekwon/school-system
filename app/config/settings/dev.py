from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
import os

SECRETS = SECRETS_FULL['base']

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS += []
INSTALLED_APPS += []
