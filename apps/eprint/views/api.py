from rest_framework import viewsets
from ..models import Eprint
from ..serializers import EprintSerializer


class EprintSetViews(viewsets.ModelViewSet):
    queryset = Eprint.objects.all()
    serializer_class = EprintSerializer
