from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django_extensions.db import fields
from urllib import parse


class News(models.Model):
    slug = fields.RandomCharField(
        length=12,
        unique=True,
        include_alpha=False,
        db_index=True,
        editable=False,
    )
    title = models.CharField(max_length=1024)
    content = models.TextField(blank=True, default="")
    published_at = models.DateTimeField(default=timezone.now, db_index=True)
    origin_link = models.URLField(
        max_length=1024, null=True, blank=True, unique=True
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "news"
        verbose_name_plural = "news"

    def __str__(self):
        return f"{self.title} - {self.published_at} - {self.origin_link}"

    @cached_property
    def domain(self):
        o = parse.urlparse(self.origin_link)
        return o.netloc
