from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'personnal-health-book.herokuapp.com']

DEBUG = True
CSRF_COOKIE_SECURE = False
# CSRF_TRUSTED_ORIGINS = ['https://personnal-health-book.herokuapp.com']

SESSION_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0
SECURE_SSL_REDIRECT = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False
