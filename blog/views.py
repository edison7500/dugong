# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from tagging.models import TaggedItem, Tag
from blog.models import Post

# Create your views here.

class BlogListView(ListView):
    http_method_names       = ['get']
    model                   = Post
    template_name           = 'blog/list.html'
    paginate_by             = 30
    queryset                = Post.objects.filter(status=Post.publish)


class BlogDetailView(DetailView):
    http_method_names       = ['get']
    model                   = Post
    template_name           = 'blog/detail.html'
    slug_field              = 'slug'


class PostTagListView(ListView):
    http_method_names       = ['get']
    model                   = TaggedItem
    template_name           = 'blog/tag/list.html'
    paginate_by             = 30

    def get_queryset(self):
        thing_tag = Tag.objects.get(pk=self.tag_id)
        # log.info(thing_tag)
        queryset  = TaggedItem.objects.get_by_model(Post, thing_tag)
        return queryset

    def get(self, request, *args, **kwargs):
        self.tag_id     = kwargs.pop('tag_id', None)
        assert self.tag_id is not None
        return super(PostTagListView, self).get(request, *args, **kwargs)