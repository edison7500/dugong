import logging

from django.contrib.postgres.search import SearchQuery, SearchVector
# from haystack.generic_views import SearchView
from django.views import generic

from apps.blog.models import Post

logger = logging.getLogger("django")


class IndexSearchView(generic.ListView):
    template_name = "search/index.html"
    model = Post
    vector = SearchVector("title", "content")
    ordering = ["-created_at"]

    def get_search_query(self):
        keywords = self.request.GET.get("q")
        return SearchQuery(keywords)

    def get_queryset(self):
        _keywords = self.get_search_query()
        if _keywords:
            qs = Post.objects.annotate(search=self.vector).filter(
                search=_keywords
            )
        else:
            qs = Post.objects.none()
        return qs

    def get_context_data(self, *args, **kwargs):
        _context = super().get_context_data(*args, **kwargs)
        _context.update({"query": self.get_search_query().value})
        return _context
