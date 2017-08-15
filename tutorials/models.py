from django.conf import settings
from django.db import models
from django.utils import timezone
from tagging.registry import register


class Tutorial(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='tutorial')
    title = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True)
    content = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    updated_datetime = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    def __str__(self):
        return '{}'.format(self.title)

register(Tutorial)
