from django.db import models
from django_markdown.models import MarkdownField

# Create your models here.


class Project(models.Model):

    title               = models.CharField(default='', max_length=255)
    desc                = models.TextField(null=True)
    github_url          = models.URLField(default='')
    readme              = MarkdownField(null=True)
    watch               = models.PositiveIntegerField(default=0, editable=False)
    star                = models.PositiveIntegerField(default=0, editable=False)
    fork                = models.PositiveIntegerField(default=0, editable=False)
    updated_datetime    = models.DateTimeField(auto_now=True, db_index=True)
