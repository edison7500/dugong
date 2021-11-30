from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField(blank=True, default="")
    published_at = models.DateTimeField(default=timezone.now, db_index=True)
    origin_link = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.published_at} - {self.origin_link}"
