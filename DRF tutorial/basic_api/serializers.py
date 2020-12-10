# basic_api/serializers.py
# DataFlair

from rest_framework import serializers
from basic_api.models import DRFPost


class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
