from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html
from django.utils.translation import ugettext as _
from mptt.admin import DraggableMPTTAdmin

from apps.photos.models import Category, Photo


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "name", "photo_count"]
    list_display_links = ["name"]
    MPTT_ADMIN_LEVEL_INDENT = 20

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        return qs.annotate(_photo_count=Count("photo"))

    def photo_count(self, obj):
        return obj._photo_count

    photo_count.admin_order_field = "_photo_count"


class PhotoAdmin(admin.ModelAdmin):
    list_display = [
        "photo",
        "user",
        "shape",
        "size",
        "camera",
        "lens",
        "shot_time",
        "uploaded_at",
    ]
    readonly_fields = ["user", "thumbnail"]

    fieldsets = (
        (_("photo-info"), {"fields": ("user", "thumbnail", "file")}),
        (_("photo"), {"fields": ("description", "category")}),
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
        print(obj)
        if obj.file:
            return format_html(
                f'<img src="{obj.resize_image(300)}" width="150" />'
            )
        else:
            return format_html(
                '<img src="https://static.jiaxin.im/dugong/static/img/placeholder.jpg" width="150" />'
            )

    shot_time.admin_order_field = "exif__shot_time"
    photo.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
