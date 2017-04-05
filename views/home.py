from django.views.generic import TemplateView
# from blog.models import Post
# from opensource.models import Project, Category
from haystack.query import SearchQuerySet
from silk.profiling.profiler import silk_profile


class HomeView(TemplateView):

    template_name = "index/home.html"

    def get_context_data(self, **kwargs):
        _context    = super(HomeView, self).get_context_data(**kwargs)

        _context['projects']    = SearchQuerySet().filter(display=True, category=1).order_by('-star')[:100]
        return _context

    @silk_profile(name='HomePage View')
    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)