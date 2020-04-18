from rest_framework import serializers
from .models import Eprint


class EprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eprint
        exclude = ["id"]
