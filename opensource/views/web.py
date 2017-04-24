# coding=utf-8

from django.views.generic import DetailView
from silk.profiling.profiler import silk_profile

from opensource.models import Project, Status

# from django.utils.log import getLogger

# log = getLogger('django')

from datetime import timedelta
from datetime import datetime

import pygal


class ProjectDetailView(DetailView):

    template_name   = 'opensource/detail.html'
    model           = Project
    slug_field      = 'identified_code'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        _context    = super(ProjectDetailView, self).get_context_data(**kwargs)

        _status     = Status.objects.filter(project=self.object,
                                            datetime__gte=datetime.now() - timedelta(30)
                                            )
        line_chat           = pygal.Line()
        line_chat.x_labels  = map(lambda x: x.datetime.strftime("%Y-%m-%d"), _status)
        line_chat.title     = self.object

        _context.update({
            'meta': {
                'author': self.object.author,
                # 'desc': "{author} - {desc}".format(author=self.object.author,
                #                                    desc=self.object.desc.encode('utf8')),
            },
            'chat': line_chat,
        })
        return _context

    @silk_profile(name='Project Detail View')
    def get(self, request, *args, **kwargs):
        return super(ProjectDetailView, self).get(request, *args, **kwargs)

