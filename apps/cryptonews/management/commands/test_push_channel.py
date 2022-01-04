# import json
import re
import requests

# from datetime import datetime, timedelta
from django.core.management import BaseCommand
from django.conf import settings
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer

translate_url = getattr(settings, "TRANSLATE_BOT_URL")


p = re.compile(r"^\[.*?\]")


class Command(BaseCommand):
    def handle(self, *args, **options):
        # _expire = datetime.utcnow() - timedelta(days=1)  # noqa
        news = News.objects.filter(origin_link__icontains="upbit").first()
        # print(_expire.astimezone())
        # if _expire.timestamp() < news.published_at.timestamp():
        ser = PushExchangeAnnSerializer(instance=news)
        _data = ser.data

        _title = _data["title"]
        _title = p.sub("", _title).strip()
        _data.update({"title": f"[Upbit] {_title}"})

        _data.update({"channel": "testAnnChannel"})
        requests.post(url="http://tg-bot:5000/push", json=_data)
