from django import template
from utils.render_md import md

register = template.Library()


@register.filter(is_safe=True)
def markdown(value):
    return md.convert(value)
