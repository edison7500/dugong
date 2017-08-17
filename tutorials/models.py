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
from tagging.registry import register
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices


class Tutorial(models.Model):
    STATUS = Choices('draft', 'published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='tutorial')
    title = models.CharField(_('title'), max_length=128, blank=True)
    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    status = StatusField(_('status'), choices_name='STATUS', default=STATUS.draft)
    content = models.TextField(blank=True, null=True)
    origin_link = models.URLField(max_length=255, null=True)
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    published_at = MonitorField(monitor='status', when=['published'])
    tags = TagField()

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


class TutorialImage(models.Model):
    post = models.ForeignKey(Tutorial, related_name='images')
    image = models.ImageField(upload_to='post/images')
    uploaded = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tutorials_image'