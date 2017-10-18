# coding=utf-8
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields
from django_markdown.utils import markdown
from tagging.fields import TagField
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from urlparse import urlparse
from utils.image.handlers import UUIDFilename

upload_dir = UUIDFilename('tutorial/images/')


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
    content = models.TextField(blank=True, null=True)
    origin_link = models.URLField(max_length=255, null=True, unique=True)
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    published_at = MonitorField(monitor='status', when=['published'])
    tags = TagField()

    objects = TutorialManager()

    class Meta:
        ordering = ['-published_at']
        verbose_name = u"教程"
        verbose_name_plural = u'教程'

    def __unicode__(self):
        return u'{title}'.format(title=self.title)

    def get_absolute_url(self):
        return reverse('tutorials:detail', args=[self.slug, ])

    @property
    def digest(self):
        _content = markdown(self.content)
        return strip_tags(_content)

    @property
    def domain(self):
        if self.origin_link:
            o = urlparse(self.origin_link)
            return o.netloc
        return "jiaxin.im"

    @property
    def domain_link(self):
        if self.origin_link:
            o = urlparse(self.origin_link)
            return "{scheme}://{host}".format(
                scheme=o.scheme,
                host=o.netloc,
            )
        return "http://jiaxin.im"

    @property
    def cover(self):
        cover = self.images.first()
        if cover:
            return "{image}?{process}".format( image=cover.image.url,
                                               process="imageView2/5/w/400/h/250/format/jpg/interlace/1/q/100|imageslim",
                                               )
        else:
            return ""

    def get_seo(self):

        seo_info = {
            "title": self.title,
            "desc": (self.digest[:75] + '...') if len(self.digest) > 75 else self.digest,
            "url": self.get_absolute_url(),
            "cover_url": self.cover,
            "tags": [tag.name for tag in self.tags],
        }
        return seo_info


class TutorialImage(models.Model):
    post = models.ForeignKey(Tutorial, related_name='images')
    image = models.ImageField(upload_to=upload_dir)
    is_cover = models.BooleanField(default=False)
    uploaded = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tutorials_image'
        ordering = ("-is_cover", )
