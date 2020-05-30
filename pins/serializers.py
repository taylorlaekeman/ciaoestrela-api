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

    def update(self, pin, validated_data):
        pin.cost = validated_data.get('cost', pin.cost)
        pin.is_available = validated_data.get('is_available', pin.is_available)
        pin.name = validated_data.get('name', pin.name)
        pin_image = validated_data.get('pin_image', None)
        if pin_image:
            image_url = pin_image['url']
            image = Image.objects.get(url=image_url)
            pin.pin_image = image
        pin.save()
        return pin


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'url'
        ]
