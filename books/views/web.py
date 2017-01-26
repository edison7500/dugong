from django.views.generic import ListView

from books.models import Book


class BookListView(ListView):
    http_method_names   = ['get']
    model               = Book
    template_name       = 'books/list.html'