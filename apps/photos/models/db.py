import json

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from apps.images.handlers import hexdigest_filename


class Photo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="photos", on_delete=models.CASCADE
    )
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(blank=True, default="")

    file = models.ImageField(
        upload_to=hexdigest_filename, width_field="width", height_field="height"
    )
    width = models.IntegerField(default=0, editable=False)
    height = models.IntegerField(default=0, editable=False)

    uploaded_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title

    @property
    def shape(self):
        return self.width, self.height

    @property
    def size(self):
        try:
            _size = f"{round(self.file.size / 1000)} KB"
        except FileNotFoundError:
            _size = "zero"
        return _size

    @property
    def thumb(self, size=64):
        return f"/{size}{self.file.url}"

    @property
    def lens(self):
        return self.exif.lens


class Exif(models.Model):
    photo = models.OneToOneField("Photo", related_name="exif", on_delete=models.CASCADE)
    info = JSONField()

    def info_to_dict(self) -> dict:
        return json.loads(self.info)

    @property
    def lens(self):
        return self.info_to_dict().get("LensModel")
