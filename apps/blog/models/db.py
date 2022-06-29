import logging
import re
from typing import List

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager

from apps.ext.models import CacheMixin
from apps.ext.render.md import md
from apps.images.models import Image
from .manager import PostManager

logger = logging.getLogger("django")


class Post(CacheMixin, models.Model):
    (block, preview, publish) = range(3)
    POST_STARUS_CHOICES = [
        (block, _("block")),
        (preview, _("preview")),
        (publish, _("publish")),
    ]

    title = models.CharField(_("title"), max_length=255)
    slug = models.SlugField(
        max_length=30, default="", unique=True, editable=False
    )
    content = models.TextField(blank=True)
    status = models.IntegerField(
        _("status"), choices=POST_STARUS_CHOICES, default=preview
    )
    created_at = models.DateTimeField(
        _("created_at"), auto_now_add=True, db_index=True, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated_at"), auto_now=True, db_index=True, editable=False
    )

    tags = TaggableManager(blank=True)

    images = GenericRelation(Image, related_query_name="images")

    objects = PostManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("posts")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    @cached_property
    def url(self) -> str:
        return self.get_absolute_url()

    @cached_property
    def created_at_ts(self) -> float:
        return self.created_at.timestamp()

    @cached_property
    def updated_at_ts(self) -> float:
        return self.updated_at.timestamp()

    @cached_property
    def digest(self):
        value = self.get_value_from_cache("digest")
        if value is None:
            value = strip_tags(self.html_content)
            self.set_value_to_cache("digest", value, timeout=86400)
        return value

    @cached_property
    def html_content(self):
        value = self.get_value_from_cache("html:content")
        if value is None:
            value, toc = self.render_markdown()
            self.set_value_to_cache("html:content", value, timeout=86400)
        return value

    @property
    def toc(self):
        html, toc = self.render_markdown()
        return toc

    def process_content(self):
        _content = f"{self.title}{strip_tags(self.html_content)}"
        _content = re.sub("(\\d|\\W)+", " ", _content)
        _content = re.sub(r"\s+", " ", _content)
        _content = _content.lower()
        return _content

    # def tag_list(self) -> List[str]:
    #     return self.tags.names()
    # return [o.name for o in self.tags.all()]

    @cached_property
    def tag_string(self) -> str:
        return ",".join(self.tags.names())

    def get_absolute_url(self) -> str:
        return f"/posts/{self.slug}/"

    def render_markdown(self):
        html = md.convert(self.content)
        return html, md.toc
