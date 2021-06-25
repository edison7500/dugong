import uuid

# import numpy as np
from hashlib import md5
from django.utils.deconstruct import deconstructible
from django.utils.encoding import smart_str

#
#
@deconstructible
class UUIDFilename(object):
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        uuid_filename = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        filename = f"{self.sub_path}{uuid_filename.hex}.{ext}"
        return filename


def hexdigest_filename(instance, filename):
    ext = filename.split(".")[-1]
    data = instance.file.read()
    hex = md5(data).hexdigest()
    return smart_str(f"img/{hex}.{ext}")


#
#
# def remove_image_rim(np_img, boundary=0.8):
#     # _np_img = np_img
#     h, w, c = np_img.shape
#     endpoint = 0
#     half_h = h - int(h / 2)
#     for i, row in enumerate(np_img[half_h:h]):
#         light = np.count_nonzero(row >= [250, 250, 250], axis=1)
#         light = np.count_nonzero(light >= 2)
#         dark = np.count_nonzero(row <= [5, 5, 5], axis=1)
#         dark = np.count_nonzero(dark >= 2)
#         if light / w > boundary or dark / w > boundary:
#             endpoint = i
#             break
#     if endpoint == 0:
#         return np_img
#     rim = range(endpoint + half_h, h)
#     np_img = np.delete(np_img, rim, axis=0)
#     return np_img
