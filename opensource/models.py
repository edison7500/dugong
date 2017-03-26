from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField

# Create your models here.


class Category(models.Model):
    title               = models.CharField(null=True, unique=True, max_length=50)
    created_datetime    = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title


class Project(models.Model):

    author              = models.CharField(default='', blank=True, max_length=255)
    name                = models.CharField(default='', blank=True, max_length=255)
    category            = models.ForeignKey(Category, related_name='category', null=True)
    desc                = models.TextField(null=True, blank=True)
    github_url          = models.URLField(default='', max_length=255)
    readme              = MarkdownField(blank=True, null=True)

    created_datetime    = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return "{author} / {name}".format(
            author=self.author,
            name=self.name,
        )


class Status(models.Model):
    project             = models.ForeignKey(Project, related_name='github_status')
    watch               = models.PositiveIntegerField(default=0, editable=False)
    star                = models.PositiveIntegerField(default=0, editable=False)
    fork                = models.PositiveIntegerField(default=0, editable=False)

    def __unicode__(self):
        return "Watch {watch} / Star {star} / Fork {fork}".format(
            watch=self.watch,
            star=self.star,
            fork=self.fork,
        )
