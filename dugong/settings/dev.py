import tempfile
from .base import *  # noqa
from .base import env


SECRET_KEY = env("SECRET_KEY", default="only dev replace me")

ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(BASE_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

#
# django session configure
#
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = tempfile.mktemp(dir="/tmp")
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar", ]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
    "JQUERY_URL": "//cdn.bootcss.com/jquery/2.2.4/jquery.min.js",
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1"]

# REST FRAMEWORK
# ------------------------------------------------------------------------------
# http://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    # "DEFAULT_PAGINATION_CLASS": "apps.ext.rest.pagination.ExtensionPagination",
    "PAGE_SIZE": 20,
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
}


# MEDIA_URL = "https://img.jiaxin.im/dugong/upload/"

# django storage configure
# --------------------------------------------------------------------
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN")
AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default="public-read")
AWS_QUERYSTRING_AUTH = False


# STATIC
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATICFILES_STORAGE = "apps.ext.storages.backends.s3.StaticStorage"
# STATIC_AWS_IS_GZIPPED = True
# STATIC_AWS_S3_CUSTOM_DOMAIN = env("STATIC_AWS_S3_CUSTOM_DOMAIN", default=None)
