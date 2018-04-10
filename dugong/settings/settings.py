# coding=utf-8

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rlch5d=b=i@gwuyjntbk#weuu0tne4*)b4hq1hb^h_tq-0=e@u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # 'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    # 'django_markdown',
    'django_comments',
    'bulma',

    'compressor',
    'tagging',
    'haystack',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth.registration',
    'django_extensions',
    'django_gravatar',
    'django_filters',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'markdownx',
    #
    'blog',
    'opensource',
    'tutorials',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',

)

ROOT_URLCONF = 'dugong.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'dugong.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'diskcache.DjangoCache',
        'LOCATION': '/tmp/dugong_cache',
        'SHARDS': 4,
        'DATABASE_TIMEOUT': 1.0,
        'OPTIONS': {
            'size_limit': 2 ** 32  # 4 gigabytes
        },
    },
}

CACHE_COUNT_TIMEOUT = 60

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

LOCALE_PATHS = (
    os.path.join(os.getcwd(), 'conf/locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(os.getcwd(), 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/static/'

HTML_MINIFY = True

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', '/usr/local/bin/lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    # ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.cssmin.rCSSMinFilter',
]
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

COMPRESS_OUTPUT_DIR = 'release'
COMPRESS_OFFLINE = True

'''
    session configure
'''
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = '/tmp/'

FILE_UPLOAD_HANDLERS = (
    # "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

# REDACTOR_UPLOAD = 'images/'

# '''
#     storage configure
# '''
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

'''
    rest framework
'''
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

''' django haystack

'''
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), '../whoosh_index'),
        'STORAGE': 'file',
        # 'POST_LIMIT': 128 * 1024 * 1024,
        'INCLUDE_SPELLING': True,
        'BATCH_SIZE': 100,
    },
}
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20

''' django mark-down

'''
MARKDOWN_EDITOR_SKIN = 'simple'
MARKDOWN_EXTENSIONS = ['extra', 'codehilite', 'tables', 'fenced_code']
MARKDOWN_EXTENSION_CONFIGS = {
    'codehilite': {
        'linenums': False,
    },
    'encoding': "utf-8",
}

# django extensions
SHELL_PLUS = 'ptpython'

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    }
}

LOGIN_REDIRECT_URL = '/'

GRAVATAR_DEFAULT_RATING = 'pg'
GRAVATAR_DEFAULT_IMAGE = 'identicon'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            # 'format': '[%(asctime)s.%(msecs)d] %(levelname)s [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
        },
        'error': {
            'format': '[%(asctime)s.%(msecs)d] [%(module)s:%(funcName)s:%(lineno)d]- %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': '/tmp/django.log',
            'mode': 'a',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file', ],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##
# django rest auth
##
REST_USE_JWT = True


###
#  BULMA Default settings
###
from .bulma import *
