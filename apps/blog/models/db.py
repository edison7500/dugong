import logging
import re

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from uuslug import uuslug
from apps.ext.render.md import md
from apps.images.models import Image
from .manager import PostManager

logger = logging.getLogger("django")


class Post(models.Model):
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

    @property
    def url(self) -> str:
        return self.get_absolute_url()

    @property
    def created_at_ts(self) -> float:
        return self.created_at.timestamp()

    @cached_property
    def digest(self):
        return strip_tags(self.html_content)

    @cached_property
    def html_content(self):
        html, toc = self.render_markdown()
        return html

    @cached_property
    def toc(self):
        html, toc = self.render_markdown()
        return toc

    def process_content(self):
        _content = "{}{}".format(self.title, strip_tags(self.html_content))
        _content = re.sub("(\\d|\\W)+", " ", _content)
        _content = re.sub(r"\s+", " ", _content)
        _content = _content.lower()
        return _content

    def tag_list(self):
        return [o.name for o in self.tags.all()]

    def tag_string(self):
        return ",".join(self.tag_list())

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])

    def render_markdown(self):
        html = md.convert(self.content)
        return html, md.toc

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = uuslug(self.title, instance=self, max_length=30)
        return super(Post, self).save(**kwargs)
