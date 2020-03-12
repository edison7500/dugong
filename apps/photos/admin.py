from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from apps.photos.models import Category, Photo


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "name"]
    list_display_links = ["name"]
    MPTT_ADMIN_LEVEL_INDENT = 20


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "shape", "size", "camera", "lens", "uploaded_at"]
    readonly_fields = [
        "thumbnail"
    ]

    def photo(self, obj):
        return format_html(f'<img src="{obj.thumb}" alt="{obj.title}" width="64" height="64" />')

    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumb}" alt="{obj.title}" width="64" height="64" />')

    photo.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
