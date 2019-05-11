from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from opensource.models import (Project, Status, PostProject,
                               People, Organization, Repository)
from opensource.serializers import (PeopleSerializer, OrganizationSerializer,
                                    ProjectSerializer,
                                    StatusSerializer,
                                    PostProjectSerializer, RepositorySerializer)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 1000


class OrganizationListAPIView(generics.ListCreateAPIView):
    model = Organization
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    # pagination_class = StandardResultsSetPagination
    ordering_fields = ('created_at',)


class OrganizationDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    lookup_field = 'name'


class PeopleListAPIView(generics.ListCreateAPIView):
    model = People
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter, DjangoFilterBackend,)
    ordering_fields = ('created_at',)


class RepositoryListAPIView(generics.ListCreateAPIView):
    model = Repository
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter, DjangoFilterBackend,)
    ordering_fields = ('created_at',)


class OpenSourceListAPIView(generics.ListCreateAPIView):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (OrderingFilter, DjangoFilterBackend,)
    ordering_fields = ('created_datetime',)
    filter_fields = ('display',)


class OpenSourceDetailAPIView(generics.RetrieveUpdateAPIView):
    model = Project
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'identified_code'


class OpenSourceStatusListView(generics.ListCreateAPIView):
    model = Status
    serializer_class = StatusSerializer

    def get_queryset(self):
        _queryset = Status.objects.filter(project_id=self.pid)
        return _queryset

    def get(self, request, *args, **kwargs):
        self.pid = kwargs.pop('pid', None)
        assert self.pid is not None
        return super(OpenSourceStatusListView, self).get(request, *args, **kwargs)


class PostProjectListAPIView(generics.ListAPIView):
    model = PostProject
    queryset = PostProject.objects.all()
    serializer_class = PostProjectSerializer
