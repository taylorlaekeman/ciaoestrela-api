from rest_framework.serializers import ModelSerializer

from .models import Image, Pin


class PinSerializer(ModelSerializer):
    class Meta:
        model = Pin
        fields = [
            'cost',
            'id',
            'image_url',
            'is_available',
            'name',
        ]


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'url'
        ]
