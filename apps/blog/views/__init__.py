# from django.http import Http404
# from django.views.generic import ListView, DetailView
# from django.views.generic.dates import ArchiveIndexView, YearArchiveView
# from taggit.models import Tag
#
# from apps.blog.models import Post
#
#
# class BlogListView(ArchiveIndexView):
#     model = Post
#     template_name = "blog/list.html"
#     paginate_by = 20
#     queryset = Post.objects.published().prefetch_related("tags")
#     date_field = "created_at"
#     date_list_period = "year"
#     allow_empty = True
#     allow_future = False
#
#     def get_dated_items(self):
#         qs = self.get_dated_queryset()
#         date_list = self.get_date_list(qs, ordering="DESC")[:5]
#
#         if not date_list:
#             qs = qs.none()
#
#         return date_list, qs, {}
#
#
# class BlogYearArchiveView(YearArchiveView):
#     model = Post
#     date_field = "created_at"
#     template_name = "archive/blogs/post_archive_year.html"
#     queryset = Post.objects.published().prefetch_related("tags")
#     make_object_list = True
#     allow_future = True
#     paginate_by = 20
#
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "blog/detail.html"
#     slug_field = "slug"
#     queryset = Post.objects.published().prefetch_related("tags")
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogDetailView, self).get_context_data(**kwargs)
#         context["meta"] = {
#             "title": f"{self.object.title} | Python观察员",
#             "desc": (self.object.digest[:75] + "...")
#             if len(self.object.digest) > 75
#             else self.object.digest,
#         }
#         try:
#             context["previous"] = self.object.get_previous_by_created_at()
#         except Post.DoesNotExist:
#             pass
#         try:
#             context["next"] = self.object.get_next_by_created_at()
#         except Post.DoesNotExist:
#             pass
#         return context
#
#
# class PostTagListView(ListView):
#     # http_method_names = ["get", "head"]
#     model = Post
#     queryset = Post.objects.published().prefetch_related("tags")
#     template_name = "blog/tag/list.html"
#     paginate_by = 30
#
#     def get_queryset(self):
#         try:
#             self.thing_tag = Tag.objects.get(pk=self.kwargs.pop("tid"))
#         except Tag.DoesNotExist:
#             raise Http404
#         qs = (
#             super().get_queryset().filter(tags__name__in=[self.thing_tag.name])
#         )
#         return qs
#
#     def get_context_data(self, **kwargs):
#         _context_data = super(PostTagListView, self).get_context_data(**kwargs)
#         _context_data.update({"tag": self.thing_tag})
#         return _context_data
