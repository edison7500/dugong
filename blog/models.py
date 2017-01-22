from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField
from uuslug import uuslug
from tagging.registry import register


class Post(models.Model):
    (block, preview, publish) = xrange(3)
    POST_STARUS_CHOICES = [
        (block, _('block')),
        (preview, _('preview')),
        (publish, _('publish'))
    ]

    title           = models.CharField(_('title'), max_length=255)
    slug            = models.SlugField(max_length=30, default='', unique=True, editable=False)
    content         = RedactorField(_('Text'),
                                        redactor_options={'lang'        : 'zh_cn',
                                                          'air'         : True,
                                                          'maxWidth'    : '500px',
                                                          # 'plugins'     : ['inlinestyle'],
                                                          # 'focusEnd'    : True,
                                                          'focus'       : True,
                                                          'maxHeight'   : 400,
                                                          },
                                        allow_file_upload=False)
    status          = models.IntegerField(choices=POST_STARUS_CHOICES, default=preview)
    created_date    = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)
    last_update     = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    class Meta:
        ordering    = ['-created_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/{slug}/".format(slug=self.slug)

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = uuslug(self.title, instance=self, max_length=30)
        return super(Post, self).save(**kwargs)

    @property
    def first_tag(self):
        if len(self.tags) > 0:
            t = self.tags[0]
            return t

register(Post)