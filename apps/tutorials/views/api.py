# from rest_framework import generics
from rest_framework import viewsets
from apps.tutorials.serializers import TutorialSerializer
from apps.tutorials.models import Tutorial

#
# class TutorialsListView(generics.ListAPIView):
#     serializer_class = TutorialSerializer
#     queryset = Tutorial.objects.published()
#
#
# class TutorialsDetailView(generics.RetrieveAPIView):
#     serializer_class = TutorialSerializer
#     queryset = Tutorial.objects.published()
#     lookup_field = "slug"


class TutorialsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
