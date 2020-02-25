import logging
from django.http import HttpResponse
from django.views import generic
from .mixins import ProcessImageMixin
from ..models import Photo

logger = logging.getLogger("django")


class ImageProcessView(ProcessImageMixin, generic.View):
    def get(self, request, *args, **kwargs):
        buffer, ext = self.resize_image()
        return HttpResponse(
            content=buffer.getvalue(), content_type=f"image/{ext.lower()}"
        )


class ImageListView(generic.ListView):
    model = Photo
    queryset = Photo.objects.all()
