from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from storages.utils import setting

bucket_name = getattr(settings, "AWS_STORAGE_BUCKET_NAME")


class StaticStorage(S3Boto3Storage):
    bucket_name = bucket_name
    location = "static"
    gzip = setting("STATIC_AWS_IS_GZIPPED", True)
    custom_domain = setting("STATIC_AWS_S3_CUSTOM_DOMAIN")
