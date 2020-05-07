from rest_framework.serializers import ModelSerializer

from .models import Pin


class PinSerializer(ModelSerializer):
    class Meta:
        model = Pin
        fields = [
            'cost',
            'image_url',
            'is_available',
            'name',
        ]
