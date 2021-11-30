from rest_framework import viewsets
from ..models import News
from ..serializers import CryptoNewsSerializer


class CryptoNewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = CryptoNewsSerializer
