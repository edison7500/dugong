from django import template

from ..models import Eprint

register = template.Library()


@register.inclusion_tag("eprint/snippets/categories.html")
def show_eprint_categories():
    categories = Eprint.objects.categories()
    return {
        "categories": categories,
    }
