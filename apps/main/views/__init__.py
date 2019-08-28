from haystack.generic_views import SearchView


class IndexSearchView(SearchView):
    template_name = "search/index.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by("-created_at")

