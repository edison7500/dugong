# from rest_framework import generics
from rest_framework import viewsets
from apps.tutorials.serializers import TutorialSerializer
from apps.tutorials.models import Tutorial


class TutorialsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
