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

    latest_30_day_star = indexes.IntegerField(default=0, stored=True)
    latest_30_day_fork = indexes.IntegerField(default=0, stored=True)
    latest_30_day_watch = indexes.IntegerField(default=0, stored=True)

    latest_7_day_star = indexes.IntegerField(default=0, stored=True)
    latest_7_day_fork = indexes.IntegerField(default=0, stored=True)
    latest_7_day_watch = indexes.IntegerField(default=0, stored=True)

    name_auto   = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_latest_30_day_star(self, obj):
        star_sum = obj.stats_df().star.diff().fillna(0).sum()
        return int(star_sum)

    def prepare_latest_30_day_fork(self, obj):
        fork_sum = obj.stats_df().fork.diff().fillna(0).sum()
        return int(fork_sum)
    #
    def prepare_latest_30_day_watch(self, obj):
        watch_sum = obj.stats_df().watch.diff().fillna(0).sum()
        return int(watch_sum)

    def prepare_latest_7_day_star(self, obj):
        star_sum = obj.stats_df(8).star.diff().fillna(0).sum()
        return int(star_sum)

    def prepare_latest_7_day_fork(self, obj):
        fork_sum = obj.stats_df(8).fork.diff().fillna(0).sum()
        return int(fork_sum)
    #
    def prepare_latest_7_day_watch(self, obj):
        watch_sum = obj.stats_df(8).watch.diff().fillna(0).sum()
        return int(watch_sum)
