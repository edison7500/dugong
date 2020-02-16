import pygal
import logging
from django.views import generic
from apps.exchangerates.models import ExChangeRate

logger = logging.getLogger("django")


class ExChangeRateListView(generic.ListView):
    model = ExChangeRate
    queryset = ExChangeRate.objects.all()
    paginate_by = 14

    def render_to_response(self, context, **response_kwargs):
        date_list = list(map(lambda x: x.date.strftime("%m-%d"), context["object_list"]))
        date_list.reverse()
        cny = list(
            map(lambda y: y.exchange_rates().get("CNY", None), context["object_list"])
        )
        cny.reverse()

        line_chart = pygal.Line()
        line_chart.title = "ExChangeRate"
        line_chart.x_labels = date_list
        line_chart.add("CNY", cny)
        return line_chart.render_django_response(**response_kwargs)
