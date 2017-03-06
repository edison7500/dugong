from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField

# Create your models here.


class Category(models.Model):
    title               = models.CharField(null=True, unique=True, max_length=50)
    created_datetime    = models.DateTimeField(default=timezone.now)


class Project(models.Model):

    title               = models.CharField(default='', max_length=255)
    category            = models.ForeignKey(Category, related_name='category', null=True)
    desc                = models.TextField(null=True)
    github_url          = models.URLField(default='', max_length=255)
    readme              = MarkdownField(null=True)
    watch               = models.PositiveIntegerField(default=0, editable=False)
    star                = models.PositiveIntegerField(default=0, editable=False)
    fork                = models.PositiveIntegerField(default=0, editable=False)
    updated_datetime    = models.DateTimeField(auto_now=True, db_index=True)
