from django.template import Library
from django.utils.log import getLogger
from tagging.models import TaggedItem
import random


log         = getLogger('django')
register    = Library()

from books.models import Book

@register.inclusion_tag('books/trending.html')
def trending_books(tags=None):
    if tags is not None:
        _books = TaggedItem.objects.get_union_by_model(Book.objects.filter(status=True), tags)
        _count = len(_books)
        if _count > 6:
            _books  = random.sample(_books, 6)
        return {'books': _books}
    else:
        return {'books': None}
    # latest_obj = Post.objects.filter(status=Post.publish)[:5]
    # log.info(latest_obj)
    # return {'posts':latest_obj}

