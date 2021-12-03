import requests
import logging
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer

logger = logging.getLogger("django")


def push_crypto_new(sender, instance: News, created, **kwargs):
    if isinstance(instance, sender) and created:
        ser = PushExchangeAnnSerializer(instance=instance)
        # logger.info(ser.data)
        requests.post(url="http://tg-bot:5000/push", json=ser.data)
