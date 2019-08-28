from haystack.generic_views import SearchView


class SearchIndexView(SearchView):
    template_name = "search/index.html"
