import uuid
import numpy as np
from django.utils.deconstruct import deconstructible


@deconstructible
class UUIDFilename(object):
    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        uuid_filename = uuid.uuid5(uuid.NAMESPACE_DNS, filename)
        filename = "{path}{filename}.{ext}".format(
            path=self.sub_path, filename=uuid_filename, ext=ext
        )
        return filename


def remove_image_rim(np_img, boundary=0.8):
    _np_img = np_img
    h, w, c = np_img.shape
    endpoint = 0
    half_h = h - int(h / 2)
    for i, row in enumerate(np_img[half_h:h]):

        light = np.count_nonzero(row >= [250, 250, 250])
        dark = np.count_nonzero(row <= [5, 5, 5])
        if light / w > boundary or dark / w > boundary:
            endpoint = i
            break
    if endpoint == 0:
        return np_img
    rim = range(endpoint + half_h, h)
    np_img = np.delete(np_img, rim, axis=0)
    return np_img
