from django.views.generic import TemplateView
from blog.models import Post



class HomeView(TemplateView):

    template_name = "index/home.html"

    def get_context_data(self, **kwargs):
        _context    = super(HomeView, self).get_context_data(**kwargs)
        latest_obj  = Post.objects.filter(status=Post.publish)[:10]
        _context['latest_posts'] = latest_obj
        return _context