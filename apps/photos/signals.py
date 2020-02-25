import json
import logging
from hashlib import md5
from pprint import pprint

from django.db.models.signals import pre_save, post_save
from django.core.cache import cache
from django.dispatch import receiver

from .models import Photo, Exif
from .utils import get_exif

logger = logging.getLogger("django")


@receiver(pre_save, sender=Photo)
def get_photo_exif(sender, instance: Photo, raw, **kwargs):
    if isinstance(instance, sender):
        _exif = get_exif(instance.file)
        key_str = f"{instance.title} - {instance.uploaded_at.timestamp()}"
        key = md5(key_str.encode("utf-8")).hexdigest()
        cache.set(key, _exif, timeout=None)


@receiver(post_save, sender=Photo)
def save_photo_exif(sender, instance: Photo, created, **kwargs):
    if created and isinstance(instance, sender):
        key_str = f"{instance.title} - {instance.uploaded_at.timestamp()}"
        key = md5(key_str.encode("utf-8")).hexdigest()
        exif = cache.get(key)
        Exif.objects.create(
            photo=instance,
            info=json.dumps(exif),
        )
