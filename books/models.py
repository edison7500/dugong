from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from tagging.registry import register
# from redactor.fields import RedactorField

# Create your models here.


class Book(models.Model):

    title               = models.CharField(max_length=255, blank=False, null=False)
    desc                = models.TextField(null=True, blank=True)
    price               = models.DecimalField(max_digits=10,
                                              decimal_places=2,
                                              default=0)
    asin                = models.CharField(max_length=255, default='')
    origin_link         = models.URLField(max_length=255, default='')
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

    def __unicode__(self):
        return self.title

    def get_purchase_link(self):

        return "{url}?tag=jiaxin05-23".format(url=self.origin_link)


register(Book)


class Image(models.Model):
    book                = models.ForeignKey(Book, related_name='images')
    image               = models.ImageField(upload_to='book/images/')
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

    def __unicode__(self):
        return self.image.url

class Purchase(models.Model):
    book                = models.ForeignKey(Book, related_name='purchases')
