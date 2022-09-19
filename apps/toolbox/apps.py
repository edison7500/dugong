"""App config for `toolbox` app."""

# For details on app configs, see:
# https://docs.djangoproject.com/en/3.2/ref/applications/

from django.apps import AppConfig


class ToolboxConfig(AppConfig):
    """App config for toolbox."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.toolbox"

    def ready(self):
        """Ready method for `toolbox` app startup."""
        # Import signals module to wire up our signal receivers.
        # https://docs.djangoproject.com/en/3.2/topics/signals/#connecting-receiver-functions
        from .models import Category
        from django.db.models.signals import pre_save
        from . import signals  # noqa

        pre_save.connect(signals.generate_slug, Category)
