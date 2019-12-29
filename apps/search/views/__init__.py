# from haystack.generic_views import SearchView
from django.views import generic
from django.contrib.postgres.search import SearchQuery, SearchVector


from apps.blog.models import Post


class IndexSearchView(generic.ListView):
    template_name = "search/index.html"
    model = Post
    vector = SearchVector("title", "content")

    def get_search_query(self):
        keywords = self.request.GET.get("q")
        return SearchQuery(keywords)

    def get_queryset(self):

        qs = Post.objects.annotate(
            search=self.vector
        ).filter(search=self.get_search_query())
        return qs.order_by("-created_at")

    def get_context_data(self, *args, **kwargs):
       _context = super().get_context_data(*args, **kwargs)
       _context.update({
           "query": self.get_search_query().value,
       })
       return _context


