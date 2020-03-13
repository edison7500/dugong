from apps.photos.models import Exif

def run():
    # print("OK")
    for row in Exif.objects.all():
        print (row.info)