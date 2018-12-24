from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
# from tutorials.models import TutorialImage
from apps.images.models import Image


class TutorialImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ['file', 'description', 'is_cover']
    extra = 1


class TutorialAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'tags', 'status', 'published_at']
    list_display_links = ['title', ]
    inlines = [TutorialImageInlineAdmin, ]
    search_fields = ['title', ]
