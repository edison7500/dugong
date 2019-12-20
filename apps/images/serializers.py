import base64
import numpy as np
from io import BytesIO
from PIL import Image
from rest_framework import serializers
from .handlers import remove_image_rim


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def _encode_image_data(self, im):
        f = BytesIO()
        im.save(f, format="jpeg")
        return base64.b64encode(f.getvalue())

    def remove_rim(self, validated_data):
        f = validated_data["image"].file
        im = Image.open(f)
        _np_img = np.array(im)
        _np_img = remove_image_rim(_np_img)

        # 旋转至 90 度
        _np_img = np.rot90(_np_img)
        _np_img = remove_image_rim(_np_img)

        # 旋转至 180 度
        _np_img = np.rot90(_np_img)
        _np_img = remove_image_rim(_np_img)

        # 旋转至 270 度
        _np_img = np.rot90(_np_img)
        _np_img = remove_image_rim(_np_img)

        # 恢复到初始位置
        _np_img = np.rot90(_np_img)
        return Image.fromarray(_np_img)

    def perform_remove_rim(self):
        im = self.remove_rim(self.validated_data)
        return {"image": self._encode_image_data(im)}
