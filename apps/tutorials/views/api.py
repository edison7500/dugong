from rest_framework import generics
from apps.tutorials.serializers import TutorialSerializer
from apps.tutorials.models import Tutorial


class TutorialsListView(generics.ListAPIView):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()


class TutorialsDetailView(generics.RetrieveAPIView):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()
    lookup_field = "slug"


# class TutorialImageListAPIView(generics.ListCreateAPIView):
#
#     serializer_class = TutorialImage
