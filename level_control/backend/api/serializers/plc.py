from rest_framework import serializers
from .models import plc


class PLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = plc
        fields = '__all__'