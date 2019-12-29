import logging

from django.views import generic

from apps.blog.models import Post
from apps.search.forms import search_form_factory

logger = logging.getLogger("django")

SearchForm = search_form_factory(
    Post.objects.filter(status=Post.publish), ["title", "content"]
)


class IndexSearchView(generic.ListView):
    template_name = "search/index.html"
    model = Post
    form = SearchForm
    ordering = ["-created_at"]
    paginate_by = 10

    def get_queryset(self):
        form = SearchForm(self.request.GET or {})
        if form.is_valid():
            qs = form.search()
        else:
            qs = Post.objects.none()
        return qs

    def get_context_data(self, *args, **kwargs):
        _context = super().get_context_data(*args, **kwargs)
        _context.update({"query": self.request.GET.get("q", "")})
        return _context
