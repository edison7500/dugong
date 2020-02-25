from PIL import Image
from PIL.ExifTags import TAGS


def get_exif(fp) -> dict:
    ret = {}
    im = Image.open(fp)
    info = im._getexif()
    for tag, value in info.items():
        decode = TAGS.get(tag, tag)
        if isinstance(value, bytes):
            _value = value.decode("utf-8").strip()
        else:
            _value = value
        ret[decode] = _value
    return ret
