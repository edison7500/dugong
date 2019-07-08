from caching.base import CachingManager, CachingMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from editormd.models import EditorMdField
from taggit.managers import TaggableManager
from uuslug import uuslug

from utils.render_md import md

from apps.images.models import Image


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
    content = EditorMdField()
    status = models.IntegerField(_('status'), choices=POST_STARUS_CHOICES, default=preview)
    created_date = models.DateTimeField(_('created_date'), auto_now_add=True, db_index=True, editable=False)
    last_update = models.DateTimeField(_('last_update'), auto_now=True, db_index=True, editable=False)

    tags = TaggableManager(blank=True)

    images = GenericRelation(Image, related_query_name="images")

    objects = CachingManager()

    class Meta:
        ordering = ['-created_date']
        verbose_name = _("posts")
        verbose_name_plural = _("posts")

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

    def tag_list(self):
        return [o.name for o in self.tags.all()]

    def tag_string(self):
        return ",".join(self.tag_list())

    def save(self, **kwargs):
        if len(self.slug) == 0:
            self.slug = uuslug(self.title, instance=self, max_length=30)
        return super(Post, self).save(**kwargs)

