import requests
from django.core.management import BaseCommand
from apps.cryptonews.models import News
from apps.cryptonews.serializers import PushExchangeAnnSerializer


class Command(BaseCommand):
    def handle(self, *args, **options):
        news = News.objects.first()
        ser = PushExchangeAnnSerializer(instance=news)
        _data = ser.data
        _data.update({"channel", "testAnnChannel"})
        print(_data)
        # requests.post(url="http://tg-bot:5000/push", json=ser.data)
