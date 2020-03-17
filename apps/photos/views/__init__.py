import logging
from django.http import HttpResponse
from django.views import generic
from .mixins import ProcessImageMixin
from ..models import Photo

logger = logging.getLogger("django")


class ImageProcessView(ProcessImageMixin, generic.View):
    def get(self, request, *args, **kwargs):
        buffer, ext = self.resize_image()
        res = HttpResponse(
            content=buffer.getvalue(), content_type=f"image/{ext.lower()}"
        )
        res["Cache-Control"] = "public, max-age=31536000"
        return res


class ImageListView(generic.ListView):
    model = Photo
    queryset = Photo.objects.all()
    template_name = "photo/index.html"
