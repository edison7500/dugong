from django.template import Library

from django.utils.log import getLogger

log = getLogger('django')

register = Library()

from blog.models import Post

@register.inclusion_tag('blog/slider/latest-update.html')
def latest_update():
    latest_obj = Post.objects.filter(status=Post.publish)[:5]
    # log.info(latest_obj)
    return {'posts':latest_obj}


# @register.inclusion_tag('base/slider/trending-article.html')
# def trending_article():
#
#
#     return