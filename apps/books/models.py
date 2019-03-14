import logging
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

from apps.images.models import Image
from apps.models.base import BaseModel

logger = logging.getLogger('django')


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

    images = GenericRelation(Image, related_query_name="images")

    class Meta:
        verbose_name = _("book")
        verbose_name_plural = _("book")

    def __str__(self):
        return self.title

    @property
    def cover(self):
        url = self.images.filter(is_cover=True).first().file.url
        return url
