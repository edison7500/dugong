from django.db import models
from django.utils import timezone

# Create your models here.


class Book(models.Model):

    title               = models.CharField(max_length=255, default='')
    desc                = models.TextField()
    price               = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    source              = models.CharField(max_length=255, default='', null=True)
    buy_link            = models.URLField(max_length=255, editable=False)
    create_datetime     = models.DateTimeField(default=timezone.now, editable=False, db_index=True)


class Image(models.Model):
    book                = models.ForeignKey(Book, related_name='images')
    image               = models.ImageField()