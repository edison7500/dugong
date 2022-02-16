import environ
import tempfile

BASE_DIR = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(BASE_DIR.path(".env")))

DEBUG = env("DJANGO_DEBUG", default=True)  # False if not in os.environ

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(BASE_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Internationalization
# -------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/topics/i18n/
TIME_ZONE = "Asia/Shanghai"

LANGUAGE_CODE = "zh-hans"

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

SITE_ID = 1

LOCALE_PATHS = (str(BASE_DIR.path("dugong/conf/locale")),)

ROOT_URLCONF = "dugong.urls"

WSGI_APPLICATION = "dugong.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.flatpages",
    "django.contrib.sitemaps",
    # "django.contrib.postgres",
]
REST_FRAMEWORK_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    # "rest_framework_simplejwt",
    # "dj_rest_auth",
    "drf_yasg",
]
THIRD_PARTY_APPS = [
    # "widget_tweaks",
    "mptt",
    "taggit",
    "django_extensions",
    "django_gravatar",
    "django_filters",
    "django_celery_beat",
    "allauth",
    "allauth.account",
]
LOCAL_APPS = [
    "apps.ext",
    "apps.blog",
    "apps.tutorials",
    "apps.images",
    "apps.photos",
    "apps.cryptonews",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = (
    DJANGO_APPS + REST_FRAMEWORK_APPS + THIRD_PARTY_APPS + LOCAL_APPS
)

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = "/tmp/static"
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(BASE_DIR.path("static"))]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
FRONTEND_DIR = str(BASE_DIR.path("frontend"))

MEDIA_URL = "/upload/"
MEDIA_ROOT = "upload/"

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
]

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(BASE_DIR.path("templates"))],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            # "string_if_invalid": 'Invalid: "%s"',
        },
    }
]

# REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "DEFAULT_PAGINATION_CLASS": "apps.ext.rest.pagination.ExtensionPagination",
    "PAGE_SIZE": 20,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "SEARCH_PARAM": "q",
}

FILE_UPLOAD_TEMP_DIR = tempfile.mkdtemp()
FILE_UPLOAD_PERMISSIONS = 0o644

# django any mail
# ----------------------------------------------------------------------------------------------------------------------
#
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {"SENDGRID_API_KEY": env("SENDGRID_API_KEY", default="<replace>")}

# django taggit
# ----------------------------------------------------------------------------------------------------------------------
#
TAGGIT_CASE_INSENSITIVE = True

# csrf view
# ----------------------------------------------------------------------------------------------------------------------
#
CSRF_FAILURE_VIEW = "apps.ext.csrf.csrf_failure"

# django allauth
# ----------------------------------------------------------------------------------------------------------------------
#
ACCOUNT_USERNAME_VALIDATORS = (
    "apps.users.validators.custom_username_validators"
)
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGOUT_ON_GET = False
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"


# REST_SESSION_LOGIN = False
REST_USE_JWT = True
OLD_PASSWORD_FIELD_ENABLED = False

# celery
# ----------------------------------------------------------------------------------------------------------------------
#
CELERY_BROKER_URL = env(
    "CELERY_BROKER_URL", default="redis://127.0.0.1:6379/12"
)
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_SERIALIZER = "msgpack"
CELERY_ACCEPT_CONTENT = ["msgpack"]

CRAWLER_URL = env("CRAWLER_URL", default="http://127.0.0.1:6800")

TRANSLATE_BOT_URL = env("TRANSLATE_BOT_URL")
