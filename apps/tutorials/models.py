from urllib.parse import urlparse

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation

# from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django_extensions.db import fields
from model_utils import Choices
from model_utils.fields import StatusField, MonitorField
from taggit.managers import TaggableManager

from apps.images.models import Image
from apps.ext.render.md import md


class TutorialManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(status="published")


class Tutorial(models.Model):
    STATUS = Choices("draft", "published")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        related_name="tutorial",
        on_delete=models.CASCADE,
    )
    title = models.CharField(_("title"), max_length=128, blank=True)
    slug = fields.RandomCharField(
        length=12,
        unique=True,
        include_alpha=False,
        db_index=True,
        editable=False,
    )
    status = StatusField(
        _("status"), choices_name="STATUS", default=STATUS.draft
    )
    content = models.TextField(blank=True, null=True)
    origin_link = models.URLField(
        _("origin_link"), max_length=255, null=True, unique=True
    )
    created_at = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False
    )
    published_at = MonitorField(monitor="status", when=["published"])

    tags = TaggableManager(blank=True)

    images = GenericRelation(Image, related_query_name="images")

    objects = TutorialManager()

    class Meta:
        ordering = ["-published_at"]
        verbose_name = _("tutorial")
        verbose_name_plural = _("tutorial")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self) -> str:
        return f"https://jiaxin.im/tutorials/{self.slug}/"

    def render_markdown(self):
        html = md.convert(self.content)
        return html, md.toc

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

    @cached_property
    def domain(self):
        if self.origin_link:
            o = urlparse(self.origin_link)
            return o.netloc
        return "jiaxin.im"

    @cached_property
    def domain_link(self):
        if self.origin_link:
            o = urlparse(self.origin_link)
            return f"{o.scheme}://{o.netloc}"
        return "https://jiaxin.im"

    @cached_property
    def cover(self):
        _covers = self.images.filter(is_cover=True)
        if _covers.count() == 0:
            return "https://static.jiaxin.im/dugong/static/img/placeholder.jpg"
        else:
            cover = _covers[0]
        return cover.file.url

    @property
    def created_at_ts(self) -> float:
        return self.created_at.timestamp()

    @property
    def published_at_ts(self) -> float:
        return self.published_at.timestamp()

    @cached_property
    def tag_list(self):
        return [{"id": o.pk, "name": o.name} for o in self.tags.all()]

    def tag_string(self):
        return ",".join(o.name for o in self.tags.all())

    #
    # def get_seo(self):
    #     seo_info = {
    #         "title": self.title,
    #         "desc": (self.digest[:75] + "...")
    #         if len(self.digest) > 75
    #         else self.digest,
    #         "url": self.get_absolute_url(),
    #         "cover_url": self.cover,
    #         "tags": self.tag_string().split(","),
    #     }
    #     return seo_info
