import base64
from django.conf import settings
from django.http import QueryDict
from django.core.files.base import ContentFile
from rest_framework.parsers import BaseParser


class Base64Parser(BaseParser):
    media_type = "application/x-www-form-urlencoded"

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}

        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)
        data = QueryDict(mutable=True)
        query_string = stream.read()
        format, imgstr = query_string.decode(encoding).split(";base64")
        ext = format.split("/")[-1]  # guess file extension
        f = ContentFile(base64.b64decode(imgstr), name=ext)
        data.appendlist(key="file", value=f)
        return data
