from django.views.generic import ListView
from tutorials.models import Tutorial


class TutorialListView(ListView):
    template_name = 'tutorials/list.html'
    model = Tutorial
    queryset = Tutorial.objects.all()
    paginate_by = 20




