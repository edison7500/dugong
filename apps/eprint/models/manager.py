from django.db import models
from django.db.models import Count


class EprintManager(models.Manager):
    def categories(self):
        return (
            self.filter(category__isnull=False)
            .values("category")
            .annotate(eprint_count=Count("category"))
            .order_by("-eprint_count")
        )
