from datetime import timedelta
from datetime import datetime
from django.views import generic
from opensource.models import Project, Status

import pygal
from pygal.style import DarkSolarizedStyle


class ProjectDetailView(generic.DetailView):
    template_name = 'opensource/detail.html'
    model = Project
    queryset = Project.objects.all()
    slug_field = 'identified_code'

    def get_context_data(self, **kwargs):
        _context = super(ProjectDetailView, self).get_context_data(**kwargs)

        _status = Status.objects.filter(project=self.object,
                                        datetime__gte=datetime.now() - timedelta(31)
                                        ).order_by('datetime')
        chart = self.get_chart(_status)

        _context.update({
            'meta': {
                'author': self.object.author,
            },
            'chart': chart.render_data_uri(show_dots=True),
        })
        return _context

    def get_chart(self, stats):
        df = stats.to_dataframe(index='datetime')

        line_chat = pygal.Line(x_label_rotation=90,
                               width=600, height=300,
                               pretty_print=True,
                               interpolate='cubic', style=DarkSolarizedStyle)
        line_chat.human_readable = True
        line_chat.x_labels = map(lambda x: x.datetime.strftime("%Y-%m-%d"), stats[1:])
        star_se = df.star.diff().fillna(0)
        fork_se = df.fork.diff().fillna(0)
        watch_se = df.watch.diff().fillna(0)
        line_chat.add('star', [row for row in star_se[1:]])
        line_chat.add('fork', [row for row in fork_se[1:]])
        line_chat.add('watch', [row for row in watch_se[1:]])
        line_chat.title = self.object.name
        return line_chat
