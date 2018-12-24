from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields
from tagging.fields import TagField
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from editormd.models import EditorMdField
from urllib.parse import urlparse
from utils.render_md import md

from apps.images.models import Image


# upload_dir = UUIDFilename('tutorial/images/')


class TutorialManager(models.Manager):

    def published(self):
        return self.get_queryset().filter(status="published")


class Tutorial(models.Model):
    STATUS = Choices('draft', 'published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='tutorial')
    title = models.CharField(_('title'), max_length=128, blank=True)
    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    status = StatusField(_('status'), choices_name='STATUS', default=STATUS.draft)
    content = EditorMdField(blank=True, null=True)
    origin_link = models.URLField(_('origin_link'), max_length=255, null=True, unique=True)
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    published_at = MonitorField(monitor='status', when=['published'])
    tags = TagField(_('tags'))

    images = GenericRelation(Image, related_query_name="images")

    objects = TutorialManager()

    class Meta:
        ordering = ['-published_at']
        verbose_name = u"教程"
        verbose_name_plural = u'教程'

    def __str__(self):
        return u'{title}'.format(title=self.title)

    def get_absolute_url(self):
        return reverse('tutorials:detail', args=[self.slug, ])

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
            return "{scheme}://{host}".format(
                scheme=o.scheme,
                host=o.netloc,
            )
        return "https://jiaxin.im"

    @property
    def cover(self):
        cover = self.images.first()
        if cover:
            return "{image}?{process}".format(image=cover.image.url,
                                              process="imageView2/5/w/400/h/250/format/jpg/interlace/1/q/100|imageslim",
                                              )
        else:
            return ""

    def tag_list(self):
        return [{"id": o.pk, "name": o.name} for o in self.tags]

    def get_seo(self):

        seo_info = {
            "title": self.title,
            "desc": (self.digest[:75] + '...') if len(self.digest) > 75 else self.digest,
            "url": self.get_absolute_url(),
            "cover_url": self.cover,
            "tags": self.tags.split(','),
        }
        return seo_info

# class TutorialImage(models.Model):
#     post = models.ForeignKey(Tutorial, related_name='images')
#     image = models.ImageField(upload_to=upload_dir)
#     is_cover = models.BooleanField(default=False)
#     uploaded = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         db_table = 'tutorials_image'
#         ordering = ("-is_cover",)
