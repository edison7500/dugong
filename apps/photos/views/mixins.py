import io

from PIL import Image
from django.core.files.storage import default_storage
from django.http import Http404


class ProcessImageMixin(object):
    def resize_image(self):
        _size = self.kwargs.get("size", 300)
        _filename = self.kwargs.get("filename", None)
        assert _filename is not None, Http404
        try:
            data = default_storage.open(f"img/{_filename}").read()
        except FileNotFoundError:
            raise Http404
        im = Image.open(io.BytesIO(data))
        im.thumbnail((_size, _size))
        buffer = io.BytesIO()
        im.save(buffer, im.format)
        return buffer, im.format
