from django.urls import reverse
from django.views import generic
from apps.images.models import Image
from apps.images.forms import ImageForm, RemoveRimFrom


class ImageListView(generic.ListView):
    model = Image
    queryset = Image.objects.all()
    template_name = "images/list.html"


class ImageUploadView(generic.CreateView):
    model = Image
    form_class = ImageForm
    template_name = "images/upload.html"
    success_url = "/"


class ImageRemoveRimView(generic.FormView):
    form_class = RemoveRimFrom
    template_name = "images/remove_rim.html"

    def get_success_url(self):
        return reverse("images:remove-rim")

    def form_valid(self, form):
        self.im_b64 = form.perform_remove_rim()
        return self.render_to_response(context=self.get_context_data())

    def get_context_data(self, **kwargs):
        _context = super().get_context_data(**kwargs)
        if hasattr(self, "im_b64"):
            _context.update(
                {"im_b64": str(self.im_b64, "utf-8"),}
            )
        return _context
