from django.contrib import admin

# Register your models here.
from apps.cryptonews.models import News


class CryptoNewsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "origin_link",
        "published_at",
    ]
    search_fields = ["title", "origin_link"]


admin.site.register(News, CryptoNewsAdmin)
