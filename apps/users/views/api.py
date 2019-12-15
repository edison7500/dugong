from django.contrib.auth import get_user_model
from oauth2_provider.contrib.rest_framework import TokenHasScope
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.serializers import UserDetailsSerializer


class UserDetailsView(generics.RetrieveAPIView):
    serializer_class = UserDetailsSerializer
    permission_classes = [IsAuthenticated, TokenHasScope]
    required_scopes = ["profile"]

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()
