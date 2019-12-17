from rest_framework import generics, parsers, status
from rest_framework.response import Response

from apps.ext.rest.parsers import Base64Parser
from apps.images.serializers import ImageSerializer


class RemoveImageRimAPIView(generics.GenericAPIView):
    parser_classes = [parsers.MultiPartParser, Base64Parser]
    serializer_class = ImageSerializer

    def remove_rim(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.perform_remove_rim()
        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.remove_rim(request, *args, **kwargs)
