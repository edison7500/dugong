from haystack.forms import SearchForm
from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet
from django.http import JsonResponse


class ProjectSearchView(SearchView):
    template_name   = 'search/search.html'
    form_class      = SearchForm
    paginate_by     = 10
    # queryset        = SearchQuerySet()

    def get_context_data(self, **kwargs):
        _context     = super(ProjectSearchView, self).get_context_data(**kwargs)
        return _context


def autocomplete(request):
    if request.is_ajax():
        sqs         = SearchQuerySet().autocomplete(name_auto=request.GET.get('term', ''))[:5]
        suggestions = [result.name for result in sqs]
        return JsonResponse(data={'results':suggestions})
