import re
import requests
import logging
import opencc
from datetime import datetime, timedelta
from django.conf import settings
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer
from apps.cryptonews.utils.translator import translate_text

logger = logging.getLogger("django")

debug = getattr(settings, "DEBUG")

p = re.compile(r"^\[.*?\]", re.IGNORECASE)
gate_pattern = re.compile("^gate\\.io", re.IGNORECASE)
binance_pattern = re.compile("^幣安")
# kucoin_pattern = re.compile(r"^kucoin", re.IGNORECASE)

hk_converter = opencc.OpenCC("hk2s")
tw_converter = opencc.OpenCC("tw2s")


def format_title(title, domain) -> str:
    _title = title
    _title = p.sub("", _title).strip()
    # _data.update({"title": f"[Upbit] {_title}"})

    if domain == "upbit.com":
        _title = f"[Upbit] {_title}"
    elif domain == "cafe.bithumb.com":
        _title = f"[Bithumb] {_title}"
    elif domain == "www.huobi.com":
        _title = hk_converter.convert(f"[Huobi] {_title}")
    elif domain == "www.gate.io":
        _title = gate_pattern.sub("", _title).strip()
        _title = f"[Gate] {_title}"
    elif domain == "www.binance.com":
        _title = binance_pattern.sub("", _title).strip()
        _title = tw_converter.convert(f"[Binance] {_title}")
    elif domain == "www.kucoin.com":
        _title = f"[KuCoin] {_title}"
        # _title = kucoin_pattern.sub("", _title).strip()
        # _title = tw_converter.convert(f"[KuCoin] {_title}")

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
