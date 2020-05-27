from rest_framework.serializers import ModelSerializer, URLField

from .models import Image, Pin


class PinSerializer(ModelSerializer):
    image_url = URLField(source='pin_image.url')

    class Meta:
        model = Pin
        fields = [
            'cost',
            'id',
            'image_url',
            'is_available',
            'name',
        ]

    def create(self, validated_data):
        image_url = validated_data.pop('pin_image')['url']
        image = Image.objects.get(url=image_url)
        return Pin.objects.create(pin_image=image, **validated_data)


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'url'
        ]
