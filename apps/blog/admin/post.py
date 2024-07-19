# from ajax_select import register, LookupChannel
# from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

# from martor.widgets import AdminMartorWidget

from apps.images.models import Image


class PostImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ["file", "description"]
    extra = 1


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "title",
        "slug",
        "status",
        "tag_string",
        "created_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("title",)
    list_per_page = 30
    inlines = (PostImageInlineAdmin,)

    # formfield_overrides = {
    #     models.TextField: {"widget": AdminMartorWidget},
    # }

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")
