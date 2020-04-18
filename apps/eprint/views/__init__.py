from django.views import generic
from ..models import Eprint


class EprintListView(generic.ListView):
    model = Eprint
    queryset = Eprint.objects.all()
    paginate_by = 30
    template_name = "eprint/list.html"


class EprintDetailView(generic.DetailView):
    model = Eprint
    queryset = Eprint.objects.all()
    slug_url_kwarg = "slug"
    slug_field = "slug"
    template_name = "eprint/detail.html"
