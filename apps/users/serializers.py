from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', 'username')