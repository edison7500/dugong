from django import template

from ..models import Eprint

register = template.Library()


@register.inclusion_tag("eprint/snippets/categories.html")
def show_eprint_categories():
    categories = Eprint.objects.categories()
    return {
        "categories": categories,
    }


@register.inclusion_tag("eprint/snippets/authors.html")
def show_eprint_authors():
    authors = Eprint.objects.authors()[:10]
    return {
        "authors": authors,
    }


@register.inclusion_tag("eprint/snippets/keywords.html")
def show_eprint_keywords():
    keywords = Eprint.objects.keywords().filter(eprint_count__gt=5)
    return {
        "keywords": keywords,
    }
