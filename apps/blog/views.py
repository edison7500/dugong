# coding=utf-8
from django.views.generic import ListView, DetailView
from tagging.models import TaggedItem, Tag

from apps.blog.models import Post


# from markdown import markdown


class BlogListView(ListView):
    http_method_names = ['get', 'head']
    model = Post
    template_name = 'blog/list.html'
    paginate_by = 20
    queryset = Post.objects.filter(status=Post.publish)


class BlogDetailView(DetailView):
    http_method_names = ['get', 'head']
    model = Post
    template_name = 'blog/detail.html'
    slug_field = 'slug'
    queryset = Post.objects.filter(status=Post.publish)

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['meta'] = {
            'title': u"{title} | Python观察员".format(title=self.object.title),
            'desc': (self.object.digest[:75] + '...') if len(self.object.digest) > 75 else self.object.digest
        }
        try:
            context['previous'] = self.object.get_previous_by_created_date()
        except Post.DoesNotExist as e:
            pass
        try:
            context['next'] = self.object.get_next_by_created_date()
        except Post.DoesNotExist as e:
            pass

        return context


class PostTagListView(ListView):
    http_method_names = ['get']
    model = TaggedItem
    template_name = 'blog/tag/list.html'
    paginate_by = 30

    def get_queryset(self):
        self.thing_tag = Tag.objects.get(pk=self.tag_id)
        queryset = TaggedItem.objects.get_by_model(Post.objects.filter(status=Post.publish),
                                                   self.thing_tag)
        return queryset

    def get_context_data(self, **kwargs):
        _context_data = super(PostTagListView, self).get_context_data(**kwargs)
        _context_data.update(
            {
                'tag':self.thing_tag,
            }
        )
        return _context_data

    def get(self, request, *args, **kwargs):
        self.tag_id = kwargs.pop('tag_id', None)
        assert self.tag_id is not None
        return super(PostTagListView, self).get(request, *args, **kwargs)
