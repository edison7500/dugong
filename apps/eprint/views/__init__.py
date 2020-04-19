from django.views import generic

from ..filters import EprintFilterSet
from ..models import Eprint


class EprintListView(generic.ListView):
    model = Eprint
    queryset = Eprint.objects.all()
    paginate_by = 30
    template_name = "eprint/list.html"

    @property
    def category(self):
        return self.request.GET.get("category", None)

    def get_queryset(self):
        qs = super().get_queryset()
        eprint_filter_list = EprintFilterSet(self.request.GET, queryset=qs)
        return eprint_filter_list.qs

    def get_context_data(self, **kwargs):
        _context = super().get_context_data(**kwargs)
        _context.update({
            "category": self.category,
        })
        return _context


class EprintDetailView(generic.DetailView):
    model = Eprint
    queryset = Eprint.objects.all()
    slug_url_kwarg = "slug"
    slug_field = "slug"
    template_name = "eprint/detail.html"
