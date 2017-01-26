# coding=utf-8
"""
Django settings for dugong project.

Generated by 'django-admin startproject' using Django 1.8.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

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

SITE_ID       = 1


# Application definition

INSTALLED_APPS = (
    'suit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',

    'redactor',
    'compressor',
    'tagging',
    'rest_framework',
    'rest_framework.authtoken',

    'blog',
    'books',
    'articles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dugong.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
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
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/django_cache',
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST    = True

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

STATIC_URL               = '/static/'
STATIC_ROOT             = '/tmp/static/'


COMPRESS_ENABLED        = False
COMPRESS_PRECOMPILERS   = (
    # ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
    # ('text/x-sass', 'sass {infile} {outfile}'),
    # ('text/x-scss', 'sass --scss {infile} {outfile}'),
)
COMPRESS_OUTPUT_DIR     = 'release'
COMPRESS_OFFLINE        = True


'''
    session configure
'''
SESSION_ENGINE          = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH       = '/tmp/'

FILE_UPLOAD_HANDLERS   = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
)

REDACTOR_UPLOAD         = 'images/'

'''
    storage configure
'''
DEFAULT_FILE_STORAGE        = 'qiniustorage.backends.QiniuStorage'

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
IMAGE_HOST                  = '//imgjiaxin.u.qiniudn.com/'

QINIU_ACCESS_KEY            = "xD6MU4_jZANfAqu9auFQm4qkSIx_ln2hIefKIFAU"
QINIU_SECRET_KEY            = "NkTHwgTFQHFaujEB3Fo-ZC2jgf6LkjkWT0iWbwWP"
QINIU_BUCKET_NAME           = "imgjiaxin"

QINIU_BUCKET_DOMAIN         = 'imgjiaxin.u.qiniudn.com'
QINIU_SECURE_URL            = False



'''
    rest framework
'''
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.AllowAny',
    ]
}

'''
    django suit config
'''
SUIT_CONFIG = {
    'ADMIN_NAME': '家欣的天空',

    'HEADER_DATE_FORMAT': 'Y / m / d',
    'HEADER_TIME_FORMAT': 'H:i',

    # 'MENU_EXCLUDE': ('auth',),

    'LIST_PER_PAGE': 20,
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'accounts': 'icon-lock',
        'articles': 'icon-book',
        'tagging':  'icon-tags',
    },
}