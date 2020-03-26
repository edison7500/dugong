from pprint import pprint

from collections import OrderedDict
from PIL import Image
from PIL.ExifTags import TAGS
from django.utils.encoding import smart_str

ComponentsConfiguration = {0: "-", 1: "Y", 2: "Cb", 3: "Cr", 4: "R", 5: "G", 6: "B"}


def process_components_configuration(value):
    r = []
    for s in value:
        r.append(ComponentsConfiguration[s])
    return "".join(r)


def get_exif(fp) -> dict:
    ret = OrderedDict()
    im = Image.open(fp)
    info = im._getexif()
    for tag, value in info.items():
        decode = TAGS.get(tag, tag)
        if decode in ["GPSInfo", "CFAPattern"]:
            continue
        elif decode == "ComponentsConfiguration":
            value = process_components_configuration(value)
        if isinstance(value, bytes):
            _value = smart_str(value)
        else:
            _value = value
        ret[decode] = _value
    return ret
