from django.db import models
from django.utils import timezone
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from caching.base import CachingManager, CachingMixin
from hashlib import md5
# Create your models here.
from django_markdown.utils import markdown


class Category(models.Model):
    title               = models.CharField(null=True, unique=True, max_length=50)
    created_datetime    = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name        = _('category')
        verbose_name_plural = _('categories')


class Project(CachingMixin, models.Model):

    author              = models.CharField(blank=True, max_length=255)
    name                = models.CharField(blank=True, max_length=255)
    category            = models.ForeignKey(Category, related_name='category', null=True)
    desc                = models.TextField(null=True, blank=True)
    github_url          = models.URLField(default='', max_length=255)
    readme              = MarkdownField(blank=True, null=True)
    created_datetime    = models.DateTimeField(auto_now=True, db_index=True)
    display             = models.BooleanField(default=True)

    identified_code     = models.CharField(null=True, blank=True, max_length=32, unique=True)

    objects             = CachingManager()

    class Meta:
        verbose_name        = _('project')
        verbose_name_plural = _('projects')

    def __unicode__(self):
        return "{author}/{name}".format(
            author=self.author,
            name=self.name,
        )

    @property
    def latest_star(self):
        _star   = 0
        try:
            stats  = self.github_status.last()
            _star   = stats.star
        except Exception as e:
            pass
        return _star

    @property
    def latest_watch(self):
        _watch      = 0
        try:
            stats   = self.github_status.last()
            _watch  = stats.watch
        except Exception as e:
            pass
        return _watch

    @property
    def latest_fork(self):
        _fork       = 0
        try:
            stats   = self.github_status.last()
            _fork   = stats.fork
        except Exception as e:
            pass
        return _fork

    def html_content(self):
        return markdown(self.readme)

    def get_subscription(self):
        return "https://github.com/{author}/{name}/subscription".format(
            author=self.author,
            name=self.name,
        )

    def get_star(self):
        return "https://github.com/{author}/{name}".format(
            author=self.author,
            name=self.name
        )

    def get_fork(self):
        return "https://github.com/{author}/{name}/fork".format(
            author=self.author,
            name=self.name
        )

    def get_absolute_url(self):
        return reverse('web-project-detail', args=[self.identified_code, ])


    def save(self, *args, **kwargs):
        if self.identified_code is None:
            self.identified_code = md5(self.github_url).hexdigest()
        super(Project, self).save(*args, **kwargs)


class Status(CachingMixin, models.Model):
    project             = models.ForeignKey(Project, related_name='github_status')
    watch               = models.PositiveIntegerField(default=0)
    star                = models.PositiveIntegerField(default=0)
    fork                = models.PositiveIntegerField(default=0)
    datetime            = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    objects             = CachingManager()

    class Meta:
        ordering    = ('datetime', )

    def __unicode__(self):
        return "Watch {watch} / Star {star} / Fork {fork}".format(
            watch=self.watch,
            star=self.star,
            fork=self.fork,
        )

class PostProject(models.Model):
    category    = models.ForeignKey(Category, )
    url         = models.URLField(max_length=255, blank=True, unique=True)
    status      = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url

    class Meta:
        db_table    = 'post_project'
