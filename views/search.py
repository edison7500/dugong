from haystack.forms import SearchForm
from haystack.generic_views import SearchView
# from haystack.query import SearchQuerySet


class ProjectSearchView(SearchView):
    template_name   = 'search/search.html'
    form_class      = SearchForm
    paginate_by     = 10
    # queryset        = SearchQuerySet()

    def get_context_data(self, **kwargs):
        _context     = super(ProjectSearchView, self).get_context_data(**kwargs)
        return _context