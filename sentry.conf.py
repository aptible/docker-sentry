from sentry.conf.server import *  # NOQA

import os
import dj_database_url
import random

DEBUG = True

SECRET_KEY = os.environ.get('SECRET_KEY', "%032x" % random.getrandbits(128))

DATABASES = {
    'default': dj_database_url.config()
}

SENTRY_KEY = os.environ.get('SENTRY_KEY', "%032x" % random.getrandbits(128))

# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_REGISTRATION = False

# The absolute URI to Sentry
SENTRY_URL_PREFIX = os.environ.get('SENTRY_URL_PREFIX', '')

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 3000
SENTRY_WEB_OPTIONS = {
    # Number of gunicorn workers
    'workers': 3
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SSLIFY_DISABLE = os.environ.get('SSLIFY_DISABLE', False)
MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
) + MIDDLEWARE_CLASSES

GITHUB_APP_ID = os.environ.get('GITHUB_APP_ID')
GITHUB_API_SECRET = os.environ.get('GITHUB_API_SECRET')
GITHUB_EXTENDED_PERMISSIONS = ['repo']
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ.get('MAILGUN_ACCESS_KEY')
MAILGUN_SERVER_NAME = os.environ.get('MAILGUN_SERVER_NAME')
