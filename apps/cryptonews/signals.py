import requests
import logging
from datetime import datetime, timedelta
from django.conf import settings
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer
from apps.cryptonews.utils.translator import translate_text

logger = logging.getLogger("django")

debug = getattr(settings, "DEBUG")


def push_crypto_new(sender, instance: News, created, **kwargs):
    if isinstance(instance, sender) and created:
        ser = PushExchangeAnnSerializer(instance=instance)
        if debug:
            logger.info(ser.data)
            return

        _expire = datetime.utcnow() - timedelta(hours=1)  # noqa
        if _expire.timestamp() < instance.published_at.timestamp():
            _data = ser.data
            if instance.domain in ["upbit.com", "cafe.bithumb.com"]:
                _title = _data["title"]
                _title = translate_text(_title, "ko", "en")
                _data.update({"title": _title})

            requests.post(url="http://tg-bot:5000/push", json=_data)
