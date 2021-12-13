import re
import requests
import logging
from datetime import datetime, timedelta
from django.conf import settings
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer
from apps.cryptonews.utils.translator import translate_text

logger = logging.getLogger("django")

debug = getattr(settings, "DEBUG")

p = re.compile(r"^\[.*?\]")


def format_title(title, domain) -> str:
    _title = title
    _title = p.sub("", _title).strip()
    # _data.update({"title": f"[Upbit] {_title}"})

    if domain == "upbit.com":
        _title = f"[Upbit] {_title}"
    elif domain == "cafe.bithumb.com":
        _title = f"[Bithumb] {_title}"
    elif domain == "www.huobi.com":
        _title = f"[Huobi] {_title}"

    return _title


def push_crypto_new(sender, instance: News, created, **kwargs):
    if isinstance(instance, sender) and created:
        ser = PushExchangeAnnSerializer(instance=instance)
        if debug:
            logger.info(ser.data)
            return

        _expire = datetime.utcnow() - timedelta(hours=1)  # noqa
        if _expire.timestamp() < instance.published_at.timestamp():
            _data = ser.data
            _title = _data["title"]

            if instance.domain in ["upbit.com", "cafe.bithumb.com"]:
                _title = translate_text(_title, "ko", "zh")

            _data.update({"title": format_title(_title, instance.domain)})
            requests.post(url="http://tg-bot:5000/push", json=_data)
