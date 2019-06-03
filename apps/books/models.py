from django.db import models
from apps.ext.models import BaseModel


# Create your models here.

class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    bio = models.TextField()

    download_link = models.URLField(max_length=255)

    def __str__(self):
        return "{} - {}".format(
            self.author, self.title
        )
