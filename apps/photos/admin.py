from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from mptt.admin import DraggableMPTTAdmin

from apps.photos.models import Category, Photo


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "name"]
    list_display_links = ["name"]
    MPTT_ADMIN_LEVEL_INDENT = 20


class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "photo",
        "shape",
        "size",
        "camera",
        "lens",
        "shot_time",
        "uploaded_at",
    ]
    readonly_fields = ["user", "thumbnail"]

    fieldsets = (
        (_("photo-info"), {"fields": ("user", "thumbnail")}),
        (_("photo"), {"fields": ("description", "category", "file")}),
    )

    list_per_page = 30

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def shot_time(self, obj):
        return obj.exif.shot_time

    def photo(self, obj):
        return format_html(f'<img src="{obj.thumb}" width="64" />')

    def thumbnail(self, obj):
        return format_html(
            f'<img src="{obj.resize_image(300)}" width="150" />'
        )

    shot_time.admin_order_field = "exif__shot_time"
    photo.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
