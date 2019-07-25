import logging

from django.template import Library
from apps.blog.models import Post

log = logging.getLogger("django")
register = Library()


@register.inclusion_tag("blog/slider/latest-update.html")
def latest_update():
    latest_obj = Post.objects.filter(status=Post.publish)[:5]
    # log.info(latest_obj)
    return {"posts": latest_obj}
