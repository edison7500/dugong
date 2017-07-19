from haystack import indexes
from opensource.models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text        = indexes.CharField(document=True, use_template=True)
    author      = indexes.CharField(model_attr='author',)
    name        = indexes.CharField(model_attr='name',)
    category    = indexes.CharField(model_attr='category')
    desc        = indexes.CharField(model_attr='desc')
    url         = indexes.CharField(model_attr='get_absolute_url')
    display     = indexes.BooleanField(model_attr='display')

    star        = indexes.IntegerField(model_attr='latest_star')
    watch       = indexes.IntegerField(model_attr='latest_watch')
    fork        = indexes.IntegerField(model_attr='latest_fork')

    latest_30_day_star = indexes.IntegerField(model_attr='latest_30_day_star')

    name_auto   = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        return self.get_model().objects.all()