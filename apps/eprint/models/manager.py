from django.db import models
from django.db.models import Count, Func, F


class EprintManager(models.Manager):
    def categories(self):
        return (
            self.filter(category__isnull=False)
            .values("category")
            .annotate(eprint_count=Count("category"))
            .order_by("-eprint_count")
        )

    def authors(self):
        return (
            self.annotate(author=Func(F("authors"), function="unnest"))
            .values("author")
            .annotate(eprint_count=Count("id"))
            .order_by("-eprint_count")
        )

    def keywords(self):
        return (
            self.annotate(keyword=Func(F("keywords"), function="unnest"))
            .values("keyword")
            .annotate(eprint_count=Count("id"))
            .order_by("-eprint_count")
        )
