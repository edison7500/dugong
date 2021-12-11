import requests
from datetime import datetime, timedelta
from django.core.management import BaseCommand
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        _expire = datetime.utcnow() - timedelta(days=1)  # noqa
        news = News.objects.first()
        # print(_expire.astimezone())
        # if _expire.timestamp() < news.published_at.timestamp():
        ser = PushExchangeAnnSerializer(instance=news)
        _data = ser.data
        _data.update({"channel": "testAnnChannel"})
        print(_data)
        requests.post(url="http://tg-bot:5000/push", json=_data)
