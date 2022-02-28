# from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from apps.tutorials.serializers import (
    TutorialSerializer,
    TutorialDetailSerializer,
)
from apps.tutorials.models import Tutorial


class TutorialsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TutorialDetailSerializer(instance)
        return Response(serializer.data)
