from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _


class BlogConfig(AppConfig):
    name = "apps.blog"
    verbose_name = _("post")

    def ready(self):
        from apps.blog.models import Post
        from apps.blog.signals import generate_slug

        pre_save.connect(generate_slug, sender=Post)
