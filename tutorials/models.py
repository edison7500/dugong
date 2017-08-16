from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields
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
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    published_at = MonitorField(monitor='status', when=['published'])
    tags = TagField()

    def __unicode__(self):
        return u'{title}'.format(title=self.title)

# register(Tutorial)
