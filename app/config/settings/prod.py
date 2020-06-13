from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
import os

SECRETS = SECRETS_FULL['prod']

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.prod.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = SECRETS['DATABASES']

ALLOWED_HOSTS += ['*']
INSTALLED_APPS += []
