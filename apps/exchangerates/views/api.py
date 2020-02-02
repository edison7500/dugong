from rest_framework import generics
from apps.exchangerates.models import ExChangeRate
from apps.exchangerates.serializers import ExChangeRateSerializer


class ExChangeRateListAPIView(generics.ListAPIView):

    serializer_class = ExChangeRateSerializer

    def get_queryset(self):
        qs = ExChangeRate.objects.all()
        return qs
