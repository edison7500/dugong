# coding=utf-8

from django.views.generic import DetailView
from opensource.models import Project



class ProjectDetailView(DetailView):

    template_name   = 'opensource/detail.html'
    model           = Project
    slug_field      = 'identified_code'
    context_object_name = 'project'
    # query_pk_and_slug =

    def get_context_data(self, **kwargs):
        _context    = super(ProjectDetailView, self).get_context_data(**kwargs)
        _context.update({
            'meta': {
                'author': self.object.author,
                'desc': "{author} - {desc}".format(author=self.object.author,
                                                   desc=self.object.desc.encode('utf8')),
            }
        })

        return _context


