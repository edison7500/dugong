from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings

from apps.images.handlers import UUIDFilename

upload_image_dir = getattr(settings, "IMAGE_UPLOAD_DIR", "images/")
upload_dir = UUIDFilename(upload_image_dir)


class ImageAbstractModel(models.Model):
    file = models.ImageField(upload_to=upload_dir)
    width = models.IntegerField(default=0, editable=False)
    height = models.IntegerField(default=0, editable=False)

    # Content-object field
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, null=True
    )
    object_id = models.PositiveIntegerField(db_index=True, null=True)
    content_object = GenericForeignKey("content_type", "object_id")

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        verbose_name = _("image")
        verbose_name_plural = _("image")
        ordering = ["-uploaded_at"]
