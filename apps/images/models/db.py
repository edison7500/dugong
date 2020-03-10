from django.db import models
from .abstracts import ImageAbstractModel


class Image(ImageAbstractModel):
    description = models.CharField(max_length=255, blank=True)
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta(ImageAbstractModel.Meta):
        db_table = "generic_image"
