# from ajax_select import register, LookupChannel
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from apps.images.models import Image


class PostImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ["file", "description"]
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "tag_string",
        "created_at",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("title",)
    list_per_page = 30
    inlines = (PostImageInlineAdmin,)

    # form = PostForm

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")
