# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.

class BlogListView(ListView):
    http_method_names = ['get']
    model = Post
    template_name = 'blog/list.html'
    paginate_by = 30
    queryset    = Post.objects.filter(status=Post.publish)


class BlogDetailView(DetailView):
    http_method_names = ['get']
    model = Post
    template_name = 'blog/detail.html'
    slug_field = 'slug'
