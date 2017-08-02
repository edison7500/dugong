from django.db import models
from django.utils import timezone


# class Category(models.Model):
#     name = models.CharField(max_length=128, blank=True)
#
#     def __str__(self):
#         return "{}".format(self.name)


class Tutorial(models.Model):
    title = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(max_length=64, unique=True)
    # category = models.ForeignKey(Category, related_name='tutorial')
    content = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    updated_datetime = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    def __str__(self):
        return '{}'.format(self.title)

