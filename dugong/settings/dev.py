from .base import *  # noqa
from .base import env

SECRET_KEY = env("SECRET_KEY", default="only dev replace me")

ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(ROOT_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

#
# django session configure
#
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = "/tmp/"

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
# INSTALLED_APPS += ["debug_toolbar", "geoip_ext"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "geoip_ext.middleware.GeoIPMiddleware",
]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
#     "SHOW_TEMPLATE_CONTEXT": True,
#     "JQUERY_URL": "//cdn.bootcss.com/jquery/2.2.4/jquery.min.js",
# }
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
# INTERNAL_IPS = ["127.0.0.1"]

#
# GEOIP database
# ----------------------------------------------------------------------------------------------------------------------
GEOIP_PATH_MMDB = str(ROOT_DIR.path("GeoLite2-Country"))

