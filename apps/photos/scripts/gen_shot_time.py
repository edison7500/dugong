from datetime import datetime
from apps.photos.models import Exif


def run():
    for row in Exif.objects.all():
        _info = row.info
        dt_string = f'{_info["DateTimeDigitized"]} +0800'
        dt = datetime.strptime(dt_string, "%Y:%m:%d %H:%M:%S %z")
        row.shot_time = dt
        row.save(force_update=True)
