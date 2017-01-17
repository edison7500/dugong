from django.db import models
from django.utils.translation import ugettext_lazy as _
from redactor.fields import RedactorField
from uuslug import uuslug
from tagging.registry import register

# Create your models here.

class Category(models.Model):
    title               = models.CharField(max_length=255, blank=True, default='')
    created_datetime    = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)

    def __unicode__(self):
        return self.title

class Article(models.Model):

    (block, draft, publish) = xrange(3)
    ARTICLE_STARUS_CHOICES = [
        (block, _('block')),
        (draft, _('draft')),
        (publish, _('publish'))
    ]

    title           = models.CharField(max_length=255, blank=True, default='')
    slug            = models.SlugField(max_length=30, default='', unique=True, editable=False)
    category        = models.ForeignKey(Category, related_name='category')
    content         = RedactorField(_('Text'),
                                        redactor_options={'lang'        : 'zh_cn',
                                                          'air'         : True,
                                                          'focus'       : True,
                                                          'maxWidth'    : 500,
                                                          'maxHeight'   : 400,
                                                          },
                                        allow_file_upload=False)
    status              = models.PositiveSmallIntegerField(choices=ARTICLE_STARUS_CHOICES, default=draft)
    created_datetime    = models.DateTimeField(db_index=True, auto_now_add=True, editable=False)
    updated_datetime    = models.DateTimeField(db_index=True, auto_now=True, editable=False)

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = uuslug(self.title, instance=self, max_length=30)
        return super(Article, self).save(**kwargs)


register(Article)