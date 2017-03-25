from rest_framework import generics
from opensource.models import Project
from opensource.serializers import ProjectSerializer


class OpenSourceListAPIView(generics.ListCreateAPIView):
    model               = Project
    queryset            = Project.objects.all()
    serializer_class    = ProjectSerializer