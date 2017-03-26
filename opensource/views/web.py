from django.views.generic import DetailView
from opensource.models import Project



class ProjectDetailView(DetailView):

    template_name   = 'opensource/detail.html'
    model           = Project
    slug_field      = 'slug'



