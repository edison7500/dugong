# from django.shortcuts import render
from django.http import Http404
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

    def get_queryset(self):
        try:
            queryset        = Post.objects.get(slug=self.get_slug_field(), status=Post.publish)
        except Post.DoesNotExist as e:
            raise Http404
        return queryset


    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['meta'] = {
            'title': self.object.title,
            'desc': (self.object.digest[:75] + '..') if len(self.object.digest) > 75 else self.object.digest
            # 'keyword': self.object.ta
        }

        return context


class PostTagListView(ListView):
    http_method_names       = ['get']
    model                   = TaggedItem
    template_name           = 'blog/tag/list.html'
    paginate_by             = 30

    def get_queryset(self):
        thing_tag = Tag.objects.get(pk=self.tag_id)
        queryset  = TaggedItem.objects.get_by_model(Post.objects.filter(status=Post.publish),
                                                    thing_tag)
        return queryset

    def get(self, request, *args, **kwargs):
        self.tag_id     = kwargs.pop('tag_id', None)
        assert self.tag_id is not None
        return super(PostTagListView, self).get(request, *args, **kwargs)