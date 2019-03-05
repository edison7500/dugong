from django.db import models
from django.utils import timezone

from apps.models.base import BaseModel


class Book(BaseModel):
    title = models.CharField(max_length=256, blank=True)
    author = models.CharField(max_length=128, blank=True)
    press = models.CharField(max_length=128, blank=True)
    version = models.CharField(max_length=30)

    license = models.CharField(max_length=64, )
    isbn = models.CharField(max_length=64, )
    format = models.CharField(max_length=30)

    brief = models.TextField()
    via = models.URLField()

    pub_date = models.DateTimeField(default=timezone.now, db_index=True, )

    def __str__(self):
        return self.title
