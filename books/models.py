from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# from redactor.fields import RedactorField

# Create your models here.


class Book(models.Model):

    title               = models.CharField(max_length=255, default='')
    desc                = models.TextField(null=True, blank=True)
    price               = models.DecimalField(max_digits=10,
                                              decimal_places=2,
                                              default=0)
    asin                = models.CharField(max_length=255, default='', editable=False)
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    book                = models.ForeignKey(Book, related_name='images')
    image               = models.ImageField(upload_to='book/images/')
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

class Purchase(models.Model):
    book                = models.ForeignKey(Book, related_name='purchases')
