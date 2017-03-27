from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from opensource.models import Project, Status, PostProject
from opensource.serializers import ProjectSerializer, StatusSerializer, PostProjectSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 100


class OpenSourceListAPIView(generics.ListCreateAPIView):
    model               = Project
    queryset            = Project.objects.all()
    serializer_class    = ProjectSerializer
    pagination_class    = StandardResultsSetPagination
    filter_backends     = (OrderingFilter, DjangoFilterBackend, )
    ordering_fields     = ('created_datetime', )
    filter_fields       = ('display', )


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


class PostProjectListAPIView(generics.ListAPIView):
    model               = PostProject
    queryset            = PostProject.objects.all()
    serializer_class    = PostProjectSerializer