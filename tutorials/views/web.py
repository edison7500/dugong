# coding=utf-8
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import Http404
from braces.views import LoginRequiredMixin, UserPassesTestMixin

from utils.views.mixins import seo
from tutorials.models import Tutorial
from tutorials.forms.tutorial import TutorialForm



class TutorialListView(ListView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/list.html'
    model = Tutorial
    queryset = Tutorial.objects.filter(status=Tutorial.STATUS.published)
    paginate_by = 12


class TutorialDetailView(seo.SEOMixin, DetailView):
    http_method_names = ['head', 'get']
    template_name = 'tutorials/detail.html'
    model = Tutorial
    # queryset = Tutorial.objects.filter(status=Tutorial.STATUS.published)
    queryset = Tutorial.objects.all()
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        _context = super(TutorialDetailView, self).get_context_data(**kwargs)
        # _context['meta'] = {
            # 'title': u"{title} | Python观察员".format(title=self.object.title),
            # 'desc': (self.object.digest[:75] + '...') if len(self.object.digest) > 75 else self.object.digest,
        # }
        _context['meta'] = self.get_seo_meta(obj=self.object)
        return _context


class TutorialCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tutorials/create.html'
    form_class = TutorialForm


class TutorialUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tutorials/update.html'
    form_class = TutorialForm
    slug_field = 'slug'
    queryset = Tutorial.objects.all()

    def get_object(self, queryset=None):
        obj = super(TutorialUpdateView, self).get_object(queryset)
        if obj.author == self.request.user:
            return obj
        else:
            raise Http404


