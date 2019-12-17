from django.views import generic
from apps.images.models import Image
from apps.images.forms import ImageForm


class ImageListView(generic.ListView):
    model = Image
    queryset = Image.objects.all()
    template_name = "images/list.html"


class ImageUploadView(generic.CreateView):
    model = Image
    form_class = ImageForm
    template_name = "images/upload.html"
    success_url = "/"
