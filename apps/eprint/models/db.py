from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django_extensions.db import fields

from apps.eprint.models.manager import EprintManager
from apps.ext.render.md import md


class Eprint(models.Model):
    slug = fields.RandomCharField(
        length=12,
        unique=True,
        include_alpha=False,
        db_index=True,
        editable=False,
    )
    title = models.CharField(max_length=255)
    authors = ArrayField(models.CharField(max_length=255,), blank=True,)
    summary = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    keywords = ArrayField(
        models.CharField(max_length=255), blank=True, default=list
    )
    origin_link = models.URLField(max_length=255, unique=True)
    received_at = models.DateField(db_index=True, null=True)
    last_revised_at = models.DateField(db_index=True, null=True)

    objects = EprintManager()

    class Meta:
        ordering = ["-received_at"]

    def __str__(self):
        return self.title

    @property
    def html_summary(self):
        return md.convert(self.summary)

    def get_absolute_url(self):
        return reverse("eprint:detail", args=[self.slug])

    def get_pdf_url(self):
        return f"{self.origin_link}.pdf"
