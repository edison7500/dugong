from django.apps import AppConfig
from django.db.models.signals import post_save


class CryptoNewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cryptonews"

    def ready(self):
        from apps.cryptonews.models import News
        from .signals import push_crypto_new

        post_save.connect(push_crypto_new, sender=News)
