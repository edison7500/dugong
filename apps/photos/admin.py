from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from apps.photos.models import Category, Photo


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "name"]
    list_display_links = ["name"]
    MPTT_ADMIN_LEVEL_INDENT = 20


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "shape", "size", "camera", "lens", "shot_time", "uploaded_at"]
    readonly_fields = ["thumbnail"]

    list_per_page = 30

    def shot_time(self, obj):
        return obj.exif.shot_time

    shot_time.admin_order_field = 'exif__shot_time'

    def photo(self, obj):
        return format_html(f'<img src="{obj.thumb}" alt="{obj.title}" width="64" />')

    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumb}" alt="{obj.title}" width="64" />')

    photo.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
