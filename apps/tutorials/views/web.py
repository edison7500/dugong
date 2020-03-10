from django.views.generic import ListView, DetailView

from apps.tutorials.models import Tutorial


class TutorialListView(ListView):
    # http_method_names = ["head", "get"]
    template_name = "tutorials/list.html"
    model = Tutorial
    queryset = Tutorial.objects.published()
    paginate_by = 12


class TutorialDetailView(DetailView):
    # http_method_names = ["head", "get"]
    template_name = "tutorials/detail.html"
    model = Tutorial
    queryset = Tutorial.objects.published()
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        _context = super(TutorialDetailView, self).get_context_data(**kwargs)
        _context["meta"] = self.object.get_seo()
        return _context


# class TutorialCreateView(LoginRequiredMixin, CreateView):
#     template_name = "tutorials/create.html"
#     form_class = TutorialForm
#
#
# class TutorialUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = "tutorials/update.html"
#     form_class = TutorialForm
#     slug_field = "slug"
#     queryset = Tutorial.objects.all()
#
#     def get_object(self, queryset=None):
#         obj = super(TutorialUpdateView, self).get_object(queryset)
#         if obj.author == self.request.user:
#             return obj
#         else:
#             raise Http404
