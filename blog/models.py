from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.utils.functional import cached_property
from markdownx.models import MarkdownxField
from uuslug import uuslug
from tagging.registry import register

# from HTMLParser import HTMLParser
# from django_markdown.models import MarkdownField
# import markdown
from utils.render_md import md

from caching.base import CachingManager, CachingMixin


# h = HTMLParser()


class Post(CachingMixin, models.Model):
    (block, preview, publish) = range(3)
    POST_STARUS_CHOICES = [
        (block, _('block')),
        (preview, _('preview')),
        (publish, _('publish'))
    ]

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(max_length=30, default='',
                            unique=True, editable=False)
    content = MarkdownxField()
    status = models.IntegerField(_('status'), choices=POST_STARUS_CHOICES, default=preview)
    created_date = models.DateTimeField(_('created_date'), auto_now_add=True, db_index=True, editable=False)
    last_update = models.DateTimeField(_('last_update'), auto_now=True, db_index=True, editable=False)

    objects = CachingManager()

    class Meta:
        ordering = ['-created_date']

    # def __unicode__(self):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])

    def render_markdown(self):
        html = md.convert(self.content)
        return html, md.toc

    @cached_property
    def digest(self):
        return strip_tags(self.html_content)

    @cached_property
    def html_content(self):
        html, toc = self.render_markdown()
        return html

    @cached_property
    def toc(self):
        html, toc = self.render_markdown()
        return toc

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = uuslug(self.title, instance=self, max_length=30)
        return super(Post, self).save(**kwargs)

    @cached_property
    def first_tag(self):
        if len(self.tags) > 0:
            t = self.tags[0]
            return t


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images')
    image = models.ImageField(upload_to='post/images')
    uploaded_datetime = models.DateTimeField(default=timezone.now)


register(Post)
