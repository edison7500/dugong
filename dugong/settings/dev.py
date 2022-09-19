from .base import *  # noqa
from .base import env

SECRET_KEY = env("SECRET_KEY", default="only dev replace me")

ALLOWED_HOSTS = ["*"]

#
# django session configure
#
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = env("SESSION_PATH", default="/tmp")
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# INSTALLED_APPS += [
# "debug_toolbar",
# ]  # noqa F405

# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.history.HistoryPanel',
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
# ]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": [
#         "debug_toolbar.panels.profiling.ProfilingPanel",
#         "debug_toolbar.panels.redirects.RedirectsPanel",
#     ],
#     'RESULTS_CACHE_SIZE': 3,
#     "SHOW_TEMPLATE_CONTEXT": True,
#     # "JQUERY_URL": "//cdn.bootcss.com/jquery/2.2.4/jquery.min.js",
# }
# # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
# INTERNAL_IPS = ["127.0.0.1"]

#
# django storage configure
# --------------------------------------------------------------------
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", default=None)
AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", default="public-read")
AWS_QUERYSTRING_AUTH = True

# STATIC
# ----------------------------------------------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# STATICFILES_STORAGE = "apps.ext.storages.backends.s3.StaticStorage"
# STATIC_AWS_IS_GZIPPED = True
# STATIC_AWS_S3_CUSTOM_DOMAIN = env("STATIC_AWS_S3_CUSTOM_DOMAIN", default=None)
