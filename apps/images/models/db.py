from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from .abstracts import ImageAbstractModel

debug = getattr(settings, "DEBUG", True)


class Image(ImageAbstractModel):
    description = models.CharField(max_length=255, blank=True)
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta(ImageAbstractModel.Meta):
        db_table = "generic_image"

    @cached_property
    def thumb(self):
        return self.resize_image()

    def resize_image(self, size=128):
        _img_url = f"/upload/{size}/{self.file.name}"
        if not debug:
            _img_url = f"https://image.jiaxin.im{_img_url}"
        return _img_url
