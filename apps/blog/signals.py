from uuslug import uuslug


def generate_slug(sender, instance, raw, using, update_fields):
    if isinstance(instance, sender) and len(instance.slug) == 0:
        # if len(instance.slug) == 0:
        instance.slug = uuslug(
            instance.title, instance=instance, max_length=30
        )
