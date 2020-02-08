from datetime import datetime
from xml.etree import ElementTree

import requests
from django.db import IntegrityError
from django_extensions.management.jobs import BaseJob

from apps.exchangerates.models import ExChangeRate

HISTORIC_RATES_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml"
LAST_90_DAYS_RATES_URL = (
    "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
)


class Job(BaseJob):
    help = "exchange rate job."

    def execute(self):
        req = requests.get(HISTORIC_RATES_URL)
        namespaces = {
            "gesmes": "http://www.gesmes.org/xml/2002-08-01",
            "eurofxref": "http://www.ecb.int/vocabulary/2002-08-01/eurofxref",
        }

        if req.status_code == 200:
            envelope = ElementTree.fromstring(req.content)
            data = envelope.findall(
                "./eurofxref:Cube/eurofxref:Cube[@time]", namespaces
            )
            for d in data:
                time = datetime.strptime(d.attrib["time"], "%Y-%m-%d").date()
                rates = {c.attrib["currency"]: float(c.attrib["rate"]) for c in list(d)}
                e = ExChangeRate()
                e.date = time
                e.rates = rates
                try:
                    e.save()
                except IntegrityError:
                    pass
