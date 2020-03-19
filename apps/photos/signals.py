import logging
from datetime import datetime
from hashlib import md5

from django.core.cache import cache
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Photo, Exif
from .utils import get_exif

logger = logging.getLogger("django")


@receiver(pre_save, sender=Photo)
def get_photo_exif(sender, instance: Photo, raw, **kwargs):
    if isinstance(instance, sender):
        _exif = get_exif(instance.file)
        key_str = f"{instance.user_id} - {instance.uploaded_at.timestamp()}"
        key = md5(key_str.encode("utf-8")).hexdigest()
        logger.info(_exif)
        setattr(instance, "width", instance.file.width)
        setattr(instance, "height", instance.file.height)
        setattr(instance, "size", instance.file.size)
        cache.set(key, _exif, timeout=None)


@receiver(post_save, sender=Photo)
def save_photo_exif(sender, instance: Photo, created, **kwargs):
    if created and isinstance(instance, sender):
        key_str = f"{instance.user_id} - {instance.uploaded_at.timestamp()}"
        key = md5(key_str.encode("utf-8")).hexdigest()
        exif = cache.get(key)
        logger.info(exif)
        Exif.objects.create(
            photo=instance,
            info=exif,
            shot_time=get_shot_time(exif)
        )


def get_shot_time(exif):
    logger.info(exif)
    dt_string = f'{exif["DateTimeDigitized"]} +0800'
    try:
        dt = datetime.strptime(dt_string, "%Y:%m:%d %H:%M:%S %z")
    except ValueError:
        dt = datetime.now()
    return dt
