from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.


class ExChangeRate(models.Model):
    date = models.DateField(db_index=True, unique=True, editable=False)
    rates = JSONField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}"
