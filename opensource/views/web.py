from django.views.generic import DetailView
from opensource.models import Project



class ProjectDetailView(DetailView):

    template_name   = 'opensource/detail.html'
    model           = Project
    slug_field      = 'identified_code'
    context_object_name = 'project'
    # query_pk_and_slug =


