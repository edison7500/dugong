from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):

    title               = models.CharField(max_length=255, default='')
    desc                = models.TextField(null=True)
    brief               = models.TextField(null=True)
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)


class Image(models.Model):
    book                = models.ForeignKey(Book, related_name='images')
    image               = models.ImageField()
    create_datetime     = models.DateTimeField(default=timezone.now,
                                               editable=False,
                                               db_index=True)

class Purchase(models.Model):
    book                = models.ForeignKey(Book, related_name='purchases')
    price               = models.DecimalField(max_digits=10,
                                              decimal_places=2,
                                              default=0)
    source              = models.CharField(max_length=30, default='')
    origin_id           = models.CharField(max_length=255, default='')