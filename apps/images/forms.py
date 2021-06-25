import logging
import base64
from io import BytesIO
from PIL import Image

# import numpy as np
from django import forms

# from .handlers import remove_image_rim
from .models import Image as ImageModel

logger = logging.getLogger("django")


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ["file", "description", "is_cover"]


#
# class RemoveRimFrom(forms.Form):
#     image = forms.ImageField(
#         widget=forms.FileInput(attrs={"class": "file-input"})
#     )
#
#     def _encode_image_data(self, im):
#         f = BytesIO()
#         im.save(f, format="jpeg")
#         return base64.b64encode(f.getvalue())
#
#     def remove_rim(self, validated_data):
#         f = validated_data.get("image")
#         im = Image.open(f)
#         _np_img = np.array(im)
#         _np_img = remove_image_rim(_np_img)
#
#         # 旋转至 90 度
#         _np_img = np.rot90(_np_img)
#         _np_img = remove_image_rim(_np_img)
#
#         # 旋转至 180 度
#         _np_img = np.rot90(_np_img)
#         _np_img = remove_image_rim(_np_img)
#
#         # 旋转至 270 度
#         _np_img = np.rot90(_np_img)
#         _np_img = remove_image_rim(_np_img)
#
#         # 恢复到初始位置
#         _np_img = np.rot90(_np_img)
#         return Image.fromarray(_np_img)
#
#     def perform_remove_rim(self):
#         im = self.remove_rim(self.cleaned_data)
#         return self._encode_image_data(im)
