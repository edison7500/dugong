import json

from django.conf import settings
from django.utils.functional import cached_property
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from apps.images.handlers import hexdigest_filename
from apps.ext.models import Category as BaseCategory

debug = getattr(settings, "DEBUG", True)


class Category(BaseCategory):
    image = models.ImageField(
        upload_to=hexdigest_filename,
        null=True,
        blank=True,
    )
    width = models.PositiveIntegerField(default=0, editable=False)
    height = models.PositiveIntegerField(default=0, editable=False)
    description = models.TextField(blank=True, default="")

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("category")

    class MPTTMeta:
        order_insertion_by = ['name']


class Photo(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="photos", on_delete=models.CASCADE
    )
    # title = models.CharField(_("title"), max_length=255)
    description = models.TextField(blank=True, default="")

    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    file = models.ImageField(
        upload_to=hexdigest_filename,
    )
    width = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    height = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    size = models.PositiveIntegerField(default=0, editable=False, db_index=True);

    uploaded_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )

    class Meta:
        ordering = ["-exif__shot_time"]

    def __str__(self):
        return f"{self.file.name} - {self.uploaded_at}"

    @property
    def shape(self):
        return self.width, self.height

    @cached_property
    def thumb(self):
        return self.resize_image()

    @property
    def camera(self):
        return self.exif.camera

    @property
    def lens(self):
        return self.exif.lens

    def resize_image(self, size=128):
        _img_url = f"/upload/{size}/{self.file.name}"
        if not debug:
            _img_url = f"https://image.jiaxin.im{_img_url}"
        return _img_url


class Exif(models.Model):
    photo = models.OneToOneField("Photo", related_name="exif", on_delete=models.CASCADE)
    info = JSONField(encoder=json.JSONEncoder)

    shot_time = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.camera} - {self.lens}"

    @property
    def camera(self):
        _make = self.info.get("Make")
        _model = self.info.get("Model")
        return f"{_make} - {_model}"

    @property
    def lens(self):
        return self.info.get("LensModel")
