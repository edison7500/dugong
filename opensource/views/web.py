# coding=utf-8

from django.views.generic import DetailView
from silk.profiling.profiler import silk_profile

from opensource.models import Project, Status

# from django.utils.log import getLogger

# log = getLogger('django')

from datetime import timedelta
from datetime import datetime

import pygal
from pygal.style import DarkSolarizedStyle


class ProjectDetailView(DetailView):

    template_name   = 'opensource/detail.html'
    model           = Project
    slug_field      = 'identified_code'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        _context    = super(ProjectDetailView, self).get_context_data(**kwargs)

        _status     = Status.objects.filter(project=self.object,
                                            datetime__gte=datetime.now() - timedelta(15)
                                            )
        line_chat           = pygal.Line(x_label_rotation=20, width=600, height=300, pretty_print=True,
                                         interpolate='cubic', style=DarkSolarizedStyle)
        line_chat.human_readable    = True
        line_chat.x_labels  = map(lambda x: x.datetime.strftime("%Y-%m-%d"), _status)
        line_chat.add('star', map(lambda x: x.star, _status))
        # line_chat.add('watch', map(lambda x: x.watch, _status))
        # line_chat.add('fork', map(lambda x: x.fork, _status))
        line_chat.title     = self.object.name

        _context.update({
            'meta': {
                'author': self.object.author,
            },
            'chat': line_chat.render(show_dots=True),
        })
        return _context

    @silk_profile(name='Project Detail View')
    def get(self, request, *args, **kwargs):
        return super(ProjectDetailView, self).get(request, *args, **kwargs)

