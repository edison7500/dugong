from controlcenter import Dashboard, widgets
from apps.blog.models import Post


class PostList(widgets.ItemList):
    model = Post
    list_display = ["id", "title", "updated_at"]
    list_display_links = "title"


class MyDashboard(Dashboard):
    widgets = (
        PostList,
    )
