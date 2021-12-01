import logging
from apps.cryptonews.models import News
from apps.cryptonews.serializers import CryptoNewsSerializer

logger = logging.getLogger("django")


def push_crypto_new(sender, instance: News, created, **kwargs):
    if isinstance(instance, sender) and created:
        ser = CryptoNewsSerializer(instance=instance)

        logger.info(ser.data)
