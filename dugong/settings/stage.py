from .base import *
from .base import env

SECRET_KEY = env("SECRET_KEY", default="only test")

ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default=str(BASE_DIR.path("db.sqlite3")))
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# django session
# -----------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/topics/http/sessions/
SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_FILE_PATH = tempfile.mkdtemp()

INSTALLED_APPS += ["django_nose"]

# Use nose to run all tests
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    "--with-coverage",
    "--cover-package=apps.blog, apps.tutorials, apps.search",
]
