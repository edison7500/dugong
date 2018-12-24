from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
from django.utils import timezone
from django.conf import settings

from apps.images.handlers import UUIDFilename

upload_image_dir = getattr(settings, "IMAGE_UPLOAD_DIR", "images/")
upload_dir = UUIDFilename(upload_image_dir)


class ImageAbstractModel(models.Model):
    file = models.ImageField(upload_to=upload_dir)
    description = models.CharField(max_length=255, blank=True)
    is_cover = models.BooleanField(default=False)

    # Content-object field
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey("content_type", "object_id")

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        verbose_name = _("photo")
        verbose_name_plural = _("photos")
        ordering = ["-uploaded_at", ]
