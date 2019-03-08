from django.contrib import admin
from apps.books.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
