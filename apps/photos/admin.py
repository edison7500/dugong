from django.contrib import admin
from django.utils.html import format_html

from apps.photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "shape", "size", "lens", "uploaded_at"]

    def photo(self, obj):
        # if obj.share_image:
        # _url = reverse("nav:share", args=[obj.slug])
        return format_html(f'<img src="{obj.thumb}" alt="{obj.title}" />')

    photo.allow_tags = True


admin.site.register(Photo, PhotoAdmin)
