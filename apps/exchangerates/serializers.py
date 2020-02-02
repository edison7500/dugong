import logging
from rest_framework import serializers
from .models import ExChangeRate


class ExChangeRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExChangeRate
