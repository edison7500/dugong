from django.contrib import admin
from books.models import Book
from books.admin.book import BookAdmin


admin.site.register(Book, BookAdmin)