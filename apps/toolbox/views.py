from rest_framework import viewsets
from .models import ToolBox
from .serializers import ToolboxSerializer


class ToolBoxAPIViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ToolboxSerializer
    queryset = ToolBox.objects.all()
