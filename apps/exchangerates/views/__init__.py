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

    # def res
    def render_to_response(self, context, **response_kwargs):
        # logger.info(context)
        date_list = list(map(lambda x: x.date, context["object_list"]))
        date_list.reverse()
        line_chart = pygal.Line()
        line_chart.title = "ExChangeRate"
        line_chart.x_labels = date_list
        cny = list(
            map(lambda y: y.exchange_rates().get("CNY", None), context["object_list"])
        )
        cny.reverse()
        line_chart.add("CNY", cny)
        return line_chart.render_django_response()
