from django.contrib import admin
from apps.books.models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "download_link", "updated_at", "created_at"]


admin.site.register(Book, BookAdmin)
