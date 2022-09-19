from hashlib import sha224
from django.template.defaultfilters import slugify
from django.utils import timezone


def get_unique_string() -> str:
    now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    h_str = sha224(now.encode("utf8")).hexdigest()
    return h_str


def generate_slug(sender, instance, *args, **kwargs):
    _slug = slugify(instance.title)
    if instance.slug != _slug and len(instance.slug) == 0:
        try:
            sender.objects.get(slug=_slug)
            instance.slug = f"{_slug}-{get_unique_string()[:8]}"
        except sender.DoesNotExist:
            instance.slug = _slug
    else:
        pass
