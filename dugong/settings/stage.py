from .base import *
from .base import env

SECRET_KEY = env('SECRET_KEY', default='only test')

ALLOWED_HOSTS = [
    "*",
]

# django session
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/http/sessions/
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = tempfile.mkdtemp()

INSTALLED_APPS += [
    'django_nose',
]

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=blog,tutorials',
]
