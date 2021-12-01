import requests
import logging
from celery import Celery
from django.conf import settings

app = Celery()

logger = logging.getLogger("django")

crawler_url = getattr(settings, "CRAWLER_URL", "http://127.0.0.1:6800")


@app.task
def run_crawler(*args, **kwargs):
    _crawler_url = f"{crawler_url}/schedule.json"

    for spider in args:
        _data = {
            "project": "default",
            "spider": spider,
        }
        r = requests.post(url=_crawler_url, data=_data)
        logger.info(f"post msg {r.status_code}")
