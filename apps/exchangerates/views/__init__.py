import pygal
import logging
from django.views import generic
from apps.exchangerates.models import ExChangeRate

logger = logging.getLogger("django")


class ExChangeRateListView(generic.ListView):
    template_name = "exchangerates/list.html"
    model = ExChangeRate
    queryset = ExChangeRate.objects.all()
    paginate_by = 14

    # def get_line_chart(self, context):
    #     # qs = self.get_queryset()
    #     line_chart = pygal.Line()
    #     line_chart.title = 'ExChangeRate'
    #     line_chart.x_labels = map(lambda x: x.date, context["object_list"])
    #     line_chart.add("CNY", map(lambda y: y.exchange_rates().get("CNY"), context["object_list"]))
    #     data = line_chart.render_data_uri()
    #     logger.info(data)
    #     return data
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     _context = super().get_context_data(**kwargs)
    #     _context.update({
    #         "chart": self.get_line_chart(_context),
    #     })
    #     return _context

    # def res
    def render_to_response(self, context, **response_kwargs):
        # logger.info(context)
        # date = map(lambda x: x.date, context["object_list"])
        line_chart = pygal.Line()
        line_chart.title = "ExChangeRate"
        line_chart.x_labels = map(lambda x: x.date, context["object_list"])
        cny = list(
            map(lambda y: y.exchange_rates().get("CNY", None), context["object_list"])
        )
        line_chart.add("CNY", cny)
        return line_chart.render_django_response()
