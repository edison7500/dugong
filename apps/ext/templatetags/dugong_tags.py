import logging
from math import floor
from urllib.parse import urlunparse, urlencode, parse_qs, urlparse

from django import template
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

register = template.Library()
logger = logging.getLogger("django")


@register.inclusion_tag("widgets/_pagination.html")
def dugong_pagination(page, **kwargs):
    pagination_kwargs = kwargs.copy()
    pagination_kwargs["page"] = page
    return get_pagination_context(**pagination_kwargs)


@register.simple_tag
def dugong_url_replace_param(url, name, value):
    return url_replace_param(url, name, value)


def url_replace_param(url, name, value):
    """Replace a GET parameter in an URL."""
    url_components = urlparse(force_str(url))
    params = parse_qs(url_components.query)
    # path = url_components.path

    if value is None:
        del params[name]
    else:
        params[name] = value
        # path = f"{url_components.path}?{name}={value}/"
    logger.info(params)

    # noinspection DjangoSafeString
    url = mark_safe(
        urlunparse(
            [
                url_components.scheme,
                url_components.netloc,
                url_components.path,
                url_components.params,
                urlencode(params, doseq=True),
                url_components.fragment,
            ]
        )
    )
    logger.info(url)
    return url


def get_pagination_context(
    page,
    pages_to_show=11,
    url=None,
    size=None,
    extra=None,
    parameter_name="page",
):
    pages_to_show = int(pages_to_show)
    if pages_to_show < 1:
        raise ValueError(
            f"Pagination pages_to_show should be a positive integer, you specified {pages_to_show}."
        )
    num_pages = page.paginator.num_pages
    current_page = page.number
    half_page_num = int(floor(pages_to_show / 2))
    if half_page_num < 0:
        half_page_num = 0
    first_page = current_page - half_page_num
    if first_page <= 1:
        first_page = 1
    if first_page > 1:
        pages_back = first_page - half_page_num
        if pages_back < 1:
            pages_back = 1
    else:
        pages_back = None
    last_page = first_page + pages_to_show - 1
    if pages_back is None:
        last_page += 1
    if last_page > num_pages:
        last_page = num_pages
    if last_page < num_pages:
        pages_forward = last_page + half_page_num
        if pages_forward > num_pages:
            pages_forward = num_pages
    else:
        pages_forward = None
        if first_page > 1:
            first_page -= 1
        if pages_back is not None and pages_back > 1:
            pages_back -= 1
        else:
            pages_back = None
    pages_shown = []
    for i in range(first_page, last_page + 1):
        pages_shown.append(i)

    # parse the url
    parts = urlparse(url or "")
    params = parse_qs(parts.query)

    # append extra querystring parameters to the url.
    if extra:
        params.update(parse_qs(extra))
    # build url again.
    url = urlunparse(
        [
            parts.scheme,
            parts.netloc,
            parts.path,
            parts.params,
            urlencode(params, doseq=True),
            parts.fragment,
        ]
    )
    pagination_css_classes = ["pagination"]
    if size == "small":
        pagination_css_classes.append("is-small")
    elif size == "large":
        pagination_css_classes.append("is-large")
    else:
        pagination_css_classes.append("is-medium")

    return {
        "dugong_pagination_url": url,
        "num_pages": num_pages,
        "current_page": current_page,
        "first_page": first_page,
        "last_page": last_page,
        "pages_shown": pages_shown,
        "pages_back": pages_back,
        "pages_forward": pages_forward,
        "pagination_css_classes": " ".join(pagination_css_classes),
        "parameter_name": parameter_name,
    }
