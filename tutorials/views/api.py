from rest_framework import generics
from tutorials.serializers import TutorialSerializer
from tutorials.models import Tutorial


class TutorialsListView(generics.ListAPIView):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()


class TutorialsDetailView(generics.RetrieveAPIView):
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.published()
    lookup_field = 'slug'
