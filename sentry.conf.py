from sentry.conf.server import *  # NOQA

import os

import dj_database_url

DEBUG = True

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': dj_database_url.config()
}

SENTRY_KEY = os.environ['SENTRY_KEY']

# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

SERVER_EMAIL = os.environ.get('SENTRY_EMAIL_FROM', 'root@localhost')

# The absolute URI to Sentry
SENTRY_URL_PREFIX = os.environ['SENTRY_URL_PREFIX']

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 3000
SENTRY_WEB_OPTIONS = {
    # Number of gunicorn workers
    'workers': 3,
    # Detect HTTPS mode from X-Forwarded-Proto header
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Uncomment to Force SSL
# MIDDLEWARE_CLASSES = \
#     ('middleware.ForceSSLMiddleware',) + MIDDLEWARE_CLASSES

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = os.environ['MAILGUN_SERVER_NAME']

GITHUB_APP_ID = os.environ['GITHUB_APP_ID']
GITHUB_API_SECRET = os.environ['GITHUB_API_SECRET']
GITHUB_EXTENDED_PERMISSIONS = ['repo']
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
