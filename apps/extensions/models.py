from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_extensions.db import fields


class BaseModel(models.Model):
    slug = fields.RandomCharField(
        length=12, unique=True,
        include_alpha=False, db_index=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        _("created_at"),
        default=timezone.now,
        db_index=True,
        editable=False
    )

    updated_at = models.DateTimeField(
        _("updated_at"),
        default=timezone.now,
        db_index=True,
        editable=False
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
