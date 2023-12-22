from django.template import loader
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.search import SearchQuery
from django.contrib.postgres.search import SearchRank
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models import Post
from apps.blog.serializers import PostSerializer


class PostSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request) -> [SearchVector, None]:
        search_fields = super().get_search_fields(view, request)
        return SearchVector(*search_fields)

    def get_search_terms(self, request) -> [SearchQuery, None]:
        params = request.query_params.get(self.search_param, "")
        if params != "":
            return SearchQuery(params)

    def filter_queryset(self, request, queryset, view):
        search_vector = self.get_search_fields(view, request)
        search_query = self.get_search_terms(request)
        if not search_vector or not search_query:
            return queryset
        return (
            queryset.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query),
            )
            .filter(search=search_query)
            .order_by("-rank")
        )

    def to_html(self, request, queryset, view):
        if not getattr(view, "search_fields", None):
            return ""

        term = request.query_params.get(self.search_param, "")
        term = term[0] if term else ""
        context = {"param": self.search_param, "term": term}
        template = loader.get_template(self.template)
        return template.render(context)


class PostAPIViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.published()
    serializer_class = PostSerializer
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
    filterset_fields = ["tags__slug"]
    filter_backends = [DjangoFilterBackend, PostSearchFilter]
    search_fields = ["title", "tags__name"]
