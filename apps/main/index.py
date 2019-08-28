# from django.views.generic import TemplateView
# from haystack.query import SearchQuerySet
#
#
# class HomeView(TemplateView):
#     template_name = "index/home.html"
#
#     def get_context_data(self, **kwargs):
#         _context = super(HomeView, self).get_context_data(**kwargs)
#         _context['projects_week'] = SearchQuerySet().filter_and(display=True,
#                                                                 category='python').order_by('-latest_7_day_star')[:20]
#         _context['projects_month'] = SearchQuerySet().filter_and(display=True,
#                                                                  category='python').order_by('-latest_30_day_star')[:20]
#         return _context
