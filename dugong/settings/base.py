import environ
import tempfile

ROOT_DIR = environ.Path(__file__) - 3  # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))

DEBUG = env("DJANGO_DEBUG", default=True)  # False if not in os.environ


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

LOCALE_PATHS = (str(ROOT_DIR.path("dugong/conf/locale")),)

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
    "rest_auth.registration",
    "drf_yasg",
]
THIRD_PARTY_APPS = [
    # "controlcenter",
    "django_comments",
    "bulma",
    "taggit",
    "taggit_serializer",
    "django_extensions",
    "django_gravatar",
    "django_filters",
    "webpack_loader",
    "oauth2_provider",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.google",
]
LOCAL_APPS = ["apps.ext", "apps.blog", "apps.tutorials", "apps.images", "apps.books"]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + REST_FRAMEWORK_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = "/tmp/static"
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(ROOT_DIR.path("static"))]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

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
        "DIRS": [str(ROOT_DIR.path("templates"))],
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
            "string_if_invalid": 'Invalid: "%s"',
        },
    }
]

# REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_PAGINATION_CLASS": "apps.ext.rest.pagination.ExtensionPagination",
    "PAGE_SIZE": 20,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
}

WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "dist/",  # must end with slash
        # 'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        "STATS_FILE": str(ROOT_DIR.path("static/webpack-stats.json")),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [".+\.hot-update.js", ".+\.map"],
    }
}

FILE_UPLOAD_TEMP_DIR = tempfile.mkdtemp()
FILE_UPLOAD_PERMISSIONS = 644

###
#  BULMA Default settings
###
from .bulma import BULMA as bulma_config

BULMA = bulma_config

SOCIALACCOUNT_PROVIDERS = {
    "google": {"SCOPE": ["profile", "email"], "AUTH_PARAMS": {"access_type": "online"}}
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "profile": "Access to user profile",
    }
}

REST_USE_JWT = True
REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "apps.users.serializers.UserDetailsSerializer"
}

#
# django any mail
#
EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"
ANYMAIL = {"SENDGRID_API_KEY": env("SENDGRID_API_KEY", default="<replace>")}

#
# django taggit
#
TAGGIT_CASE_INSENSITIVE = True

#
# GEOIP database
# ----------------------------------------------------------------------------------------------------------------------
# GEOIP_PATH_MMDB = str(ROOT_DIR.path("GeoLite2-Country"))

# django allauth
# ----------------------------------------------------------------------------------------------------------------------
ACCOUNT_USERNAME_VALIDATORS = "apps.users.validators.custom_username_validators"
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_LOGOUT_ON_GET = False
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
