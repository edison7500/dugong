from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.db import models

# Create your models here.
from django.utils import timezone


class ImageAbstractModel(models.Model):
    file = models.ImageField()
    description = models.CharField(max_length=255, blank=True)

    # Content-object field
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE)
    object_pk = models.TextField(_('object ID'))
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        verbose_name = _("photo")
        verbose_name_plural = _("photos")
