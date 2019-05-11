from django.contrib import admin
from .models import Image


# Register your models here.


class ImagesAdmin(admin.ModelAdmin):
    list_display = ['file', 'description', 'is_cover', 'content_type', 'uploaded_at']
    list_filter = ['is_cover']


admin.site.register(Image, ImagesAdmin)
