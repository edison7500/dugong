# coding=utf-8
from django.views.generic import ListView, DetailView, CreateView
from braces.views import LoginRequiredMixin
from tutorials.models import Tutorial
from tutorials.forms.tutorial import TutorialForm


class TutorialListView(ListView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/list.html'
    model = Tutorial
    queryset = Tutorial.objects.filter(status=Tutorial.STATUS.published)
    paginate_by = 20


class TutorialDetailView(DetailView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/detail.html'
    model = Tutorial
    # queryset = Tutorial.objects.filter(status=Tutorial.STATUS.published)
    queryset = Tutorial.objects.all()
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        _context = super(TutorialDetailView, self).get_context_data(**kwargs)
        _context['meta'] = {
            'title': u"{title} | Python观察员".format(title=self.object.title),
            'desc': (self.object.digest[:75] + '...') if len(self.object.digest) > 75 else self.object.digest,
        }
        return _context


class TutorialCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tutorials/create.html'
    form_class = TutorialForm
