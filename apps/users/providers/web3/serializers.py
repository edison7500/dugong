from rest_framework import serializers


class WalletSerializer(serializers.Serializer):
    address = serializers.CharField()
