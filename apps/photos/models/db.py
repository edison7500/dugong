from django.db import models
from apps.images.models.abstracts import ImageAbstractModel


class Photo(ImageAbstractModel):
    title = models.CharField(max_length=255)
