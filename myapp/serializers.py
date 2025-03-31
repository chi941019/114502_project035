from rest_framework import serializers
from .models import ButtonConfig

class ButtonConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ButtonConfig
        fields = '__all__'
