from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django_extensions.db import fields


class Eprint(models.Model):
    slug = fields.RandomCharField(
        length=12, unique=True, include_alpha=False, db_index=True, editable=False
    )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255,)
    summary = models.TextField(blank=True, null=True)
    keywords = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    origin_link = models.URLField(max_length=255, unique=True)
    published_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    def __str__(self):
        return self.title
