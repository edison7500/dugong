from .base import *
from .base import env

SECRET_KEY = env('SECRET_KEY', default='rlch5d=b=i@gwuyjntbk#weuu0tne4*)b4hq1hb^h_tq-0=e@u')

ALLOWED_HOSTS = [
    "*",
]

# django session
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/http/sessions/
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/'

INSTALLED_APPS += [
    'django_nose',
]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=blog,opensource,tutorials',
]


