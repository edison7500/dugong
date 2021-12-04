import requests
import logging
from django.conf import settings
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer

logger = logging.getLogger("django")

debug = getattr(settings, "DEBUG")


def push_crypto_new(sender, instance: News, created, **kwargs):
    if isinstance(instance, sender) and created:
        ser = PushExchangeAnnSerializer(instance=instance)
        # logger.info(ser.data)
        if debug:
            logger.info(ser.data)
        # else:
        #     requests.post(url="http://tg-bot:5000/push", json=ser.data)
