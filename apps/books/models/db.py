import hashlib
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from model_utils import Choices
from taggit.managers import TaggableManager

from apps.ext.models import BaseModel

# Create your models here.
from apps.images.models import Image


class Book(BaseModel):
    STATUS = Choices((0, "draft", _("draft")), (1, "published", _("published")))

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    origin_link = models.URLField(max_length=255, blank=True, null=True)
    download_link = models.URLField(max_length=512, blank=True, null=True)
    identified = models.CharField(
        max_length=32, null=True, db_index=True, editable=False
    )

    status = models.PositiveSmallIntegerField(choices=STATUS, default=STATUS.draft)

    tags = TaggableManager(blank=True)

    images = GenericRelation(Image, related_query_name="images")

    def __str__(self):
        return "{} - {}".format(self.author, self.title)

    def save(self, *args, **kwargs):
        if self.origin_link and self.identified is None:
            m = hashlib.md5()
            m.update(self.origin_link.encode("utf-8"))
            self.identified = m.hexdigest()
        super().save(*args, **kwargs)

    def tag_list(self):
        return [o.name for o in self.tags.all()]

    def tag_string(self):
        return ", ".join(self.tag_list())
