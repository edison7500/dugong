from haystack import indexes
from opensource.models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text        = indexes.CharField(document=True, use_template=True)
    author      = indexes.CharField(model_attr='author')
    name        = indexes.CharField(model_attr='name')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        return self.get_model().objects.all()