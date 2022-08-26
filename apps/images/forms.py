import logging
from django import forms

# from .handlers import remove_image_rim
from .models import Image as ImageModel

logger = logging.getLogger("django")


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ["file", "description", "is_cover"]
