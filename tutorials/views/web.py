from django.views.generic import ListView, DetailView
from tutorials.models import Tutorial


class TutorialListView(ListView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/list.html'
    model = Tutorial
    queryset = Tutorial.objects.all()
    paginate_by = 20


class TutorialDetailView(DetailView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/detail.html'
    model = Tutorial
    queryset = Tutorial.objects.all()
    slug_field = 'slug'




