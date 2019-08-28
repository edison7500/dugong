from haystack.generic_views import SearchView


class IndexSearchView(SearchView):
    template_name = "search/index.html"

