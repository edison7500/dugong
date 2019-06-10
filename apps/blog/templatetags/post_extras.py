import logging
from django.template import Library
# from django.utils.log import getLogger
# from tagging.models import TaggedItem
import random

log = logging.getLogger('django')
register = Library()

from apps.blog.models import Post


@register.inclusion_tag('blog/slider/latest-update.html')
def latest_update():
    latest_obj = Post.objects.filter(status=Post.publish)[:5]
    # log.info(latest_obj)
    return {'posts': latest_obj}


# @register.inclusion_tag('blog/slider/trending-article.html')
# def trending_article(tag=None):
#     trending_obj = Post.objects.filter(status=Post.publish)
#     if len(tag) > 0:
#         q = TaggedItem.objects.get_by_model(trending_obj, tag)
#         count = len(q)
#         if count > 5:
#             count = 5
#         return {'posts': random.sample(q, count)}
#     return {'posts': random.sample(trending_obj, 5)}
