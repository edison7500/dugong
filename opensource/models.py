from datetime import datetime, timedelta
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django_pandas.managers import DataFrameManager
from django_extensions.db import fields

from caching.base import CachingManager, CachingMixin
from hashlib import md5
# from markdownx.models import MarkdownxField
from utils.render_md import md


class Organization(CachingMixin, models.Model):
    slug = fields.RandomCharField(length=12, unique=True,
                                  include_alpha=False, db_index=True, editable=False)
    name = models.CharField(max_length=128)
    bio = models.CharField(max_length=255, blank=True, default='')
    location = models.CharField(max_length=255, blank=True, null=True)
    web_site = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    avatar = models.URLField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, unique=True, default='')

    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("organization")
        verbose_name_plural = _("organization")


class People(CachingMixin, models.Model):
    name = models.CharField(blank=True, null=True, max_length=128,)
    nickname = models.CharField(blank=True, max_length=128)
    bio = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    web_site = models.URLField(max_length=255, blank=True, null=True)

    avatar = models.URLField(max_length=255, blank=True, null=True)

    url = models.URLField(max_length=255, unique=True, default='')
    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = _('people')
        verbose_name_plural = _('people')
        ordering = ("-created_at",)


class Repository(models.Model):
    author = models.CharField(max_length=128, default='')
    name = models.CharField(max_length=128, default='')
    desc = models.TextField(null=True, blank=True)
    readme = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)

    identified_code = models.CharField(null=True, blank=True,
                                       max_length=32, unique=True)

    created_at = models.DateTimeField(default=timezone.now,
                                      editable=False,
                                      db_index=True)

    class Meta:
        verbose_name = _("repository")
        verbose_name_plural = _("repositories")

    def __str__(self):
        return "{author}/{name}".format(
            author=self.author,
            name=self.name,
        )

    def save(self, *args, **kwargs):
        if self.identified_code is None:
            self.identified_code = md5(self.url.encode('utf-8')).hexdigest()
        super(Repository, self).save(*args, **kwargs)


class Category(CachingMixin, models.Model):
    title = models.CharField(null=True, unique=True, max_length=50)
    created_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Project(CachingMixin, models.Model):
    author = models.CharField(blank=True, max_length=255)
    name = models.CharField(blank=True, max_length=255)
    category = models.ForeignKey(Category, related_name='category', null=True)
    desc = models.TextField(null=True, blank=True)
    github_url = models.URLField(default='', max_length=255)
    readme = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, editable=False)

    identified_code = models.CharField(null=True, blank=True, max_length=32, unique=True)

    objects = CachingManager()

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')

    def __str__(self):
        return "{author}/{name}".format(
            author=self.author,
            name=self.name,
        )

    def stats_df(self, days=31):
        return self.github_status \
            .filter(datetime__gte=datetime.now() - timedelta(days)).order_by('datetime') \
            .to_dataframe(index='datetime')

    @property
    def latest_star(self):
        _star = 0
        try:
            stats = self.github_status.first()
            _star = stats.star
        except Exception as e:
            pass
        return _star

    @property
    def latest_watch(self):
        _watch = 0
        try:
            stats = self.github_status.first()
            _watch = stats.watch
        except Exception as e:
            pass
        return _watch

    @property
    def latest_fork(self):
        _fork = 0
        try:
            stats = self.github_status.first()
            _fork = stats.fork
        except Exception as e:
            pass
        return _fork

    def html_content(self):
        return md.convert(self.readme)

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
            self.identified_code = md5(self.github_url.encode('utf-8')).hexdigest()
        super(Project, self).save(*args, **kwargs)


class Status(CachingMixin, models.Model):
    project = models.ForeignKey(Project, related_name='github_status')
    watch = models.PositiveIntegerField(default=0)
    star = models.PositiveIntegerField(default=0)
    fork = models.PositiveIntegerField(default=0)
    datetime = models.DateTimeField(default=timezone.now, db_index=True, editable=False)
    objects = DataFrameManager()

    class Meta:
        ordering = ('-datetime',)

    def __str__(self):
        return "Watch {watch} / Star {star} / Fork {fork}".format(
            watch=self.watch,
            star=self.star,
            fork=self.fork,
        )


class PostProject(models.Model):
    category = models.ForeignKey(Category, )
    url = models.URLField(max_length=255, blank=True, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, db_index=True)

    def __str__(self):
        return self.url

    class Meta:
        db_table = 'post_project'
        verbose_name = _("post project")
        verbose_name_plural = _("post projects")
        ordering = ["-created_at"]
