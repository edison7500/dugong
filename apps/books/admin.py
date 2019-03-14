from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from apps.books.models import Book
from apps.images.models import Image


class BookImageInlineAdmin(GenericStackedInline):
    model = Image
    fields = ['file', 'description', 'is_cover']
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title', 'format', 'created_at', 'updated_at']
    list_filter = ['format', ]
    list_display_links = ['title']
    inlines = [
        BookImageInlineAdmin,
    ]


admin.site.register(Book, BookAdmin)
