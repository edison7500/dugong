from rest_framework import generics
from opensource.models import Project, Status
from opensource.serializers import ProjectSerializer, StatusSerializer



class OpenSourceListAPIView(generics.ListCreateAPIView):
    model               = Project
    queryset            = Project.objects.all()
    serializer_class    = ProjectSerializer


class OpenSourceDetailAPIView(generics.RetrieveUpdateAPIView):
    model               = Project
    queryset            = Project.objects.all()
    serializer_class    = ProjectSerializer
    lookup_field        = 'identified_code'


class OpenSourceStatusListView(generics.ListCreateAPIView):
    model               = Status
    serializer_class    = StatusSerializer
    # queryset            = Status.objects.all()

    def get_queryset(self):
        _queryset       = Status.objects.filter(project_id=self.pid)
        return _queryset

    def get(self, request, *args, **kwargs):
        self.pid = kwargs.pop('pid', None)
        assert self.pid is not None
        return super(OpenSourceStatusListView, self).get(request, *args, **kwargs)