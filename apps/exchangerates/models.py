import logging
from django.db import models
from django.contrib.postgres.fields import JSONField


logger = logging.getLogger("django")
# Create your models here.


class ExChangeRate(models.Model):
    date = models.DateField(db_index=True, unique=True, editable=False)
    rates = JSONField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}"

    def exchange_rates(self, base="USD"):
        base = base.upper()
        if base != "EUC":
            base_rate = self.rates[base]
            # logger.info(base_rate)
            _rates = {
                currency: rate / base_rate for currency, rate in self.rates.items()
            }
            _rates["EUR"] = 1.0 / base_rate
        else:
            _rates = self.rates
        return _rates
