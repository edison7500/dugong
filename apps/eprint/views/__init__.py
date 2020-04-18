from django.views import generic
from ..models import Eprint


class EprintListView(generic.ListView):
    model = Eprint
    queryset = Eprint.objects.all()
    paginate_by = 30
    template_name = "eprint/list.html"
