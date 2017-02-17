from django.db import models
from django.utils import timezone
from tagging.registry import register
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):

    title               = models.CharField(_('title'), max_length=255, blank=False, null=False)
    desc                = models.TextField(null=True, blank=True)
    price               = models.DecimalField(max_digits=10,
                                              decimal_places=2,
                                              default=0)
    asin                = models.SlugField(max_length=255, unique=True, null=False)
    origin_link         = models.URLField(max_length=255, default='')
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)
    status              = models.BooleanField(_('status'), default=False)

    @property
    def image_urls(self):
        try:
            return [row.image.url for row in self.images.all()]
        except Exception as e:
            return []

    def __unicode__(self):
        return self.title

    def get_purchase_link(self):
        return "{url}?tag=jiaxin05-23".format(url=self.origin_link)

    def get_first_image_url(self):
        if len(self.image_urls) > 0:
            return self.image_urls[0]

register(Book)


class Image(models.Model):
    book                = models.ForeignKey(Book, related_name='images')
    image               = models.ImageField(upload_to='book/images/')
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

    def __unicode__(self):
        return self.image.url

# class Purchase(models.Model):
#     book                = models.ForeignKey(Book, related_name='purchases')
