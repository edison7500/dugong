from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = "apps.blog"

    def ready(self):
        pass
