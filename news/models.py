from django.db import models

# Create your models here.
from django.utils import timezone
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    title           = models.CharField(_('title'), max_length=255, null=False, blank=True)
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
    # content             = models.Ch(max_length=255, null=True, blank=True)
    created_datetime    = models.DateTimeField(default=timezone.now, db_index=True)
