from django.contrib import admin
from apps.books.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):

    list_display = [
        "identified",
        "title",
        "author",
        "download_link",
        "tag_string",
        "updated_at",
        "created_at",
    ]
    list_display_links = ["title"]


admin.site.register(Book, BookAdmin)
