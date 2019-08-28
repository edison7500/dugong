from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    created_at = indexes.DateTimeField(model_attr="created_at")
    updated_at = indexes.DateTimeField(model_attr="updated_at")

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.published()

    def get_updated_field(self):
        return "updated_at"

