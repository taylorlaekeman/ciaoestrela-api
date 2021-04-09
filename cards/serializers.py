from rest_framework.serializers import ModelSerializer, URLField

from .models import CardImage, Card


class CardSerializer(ModelSerializer):
    image_url = URLField(source='image.url')

    class Meta:
        fields = [
            'cost',
            'id',
            'image_url',
            'is_available',
            'name',
        ]
        model = Card

    def create(self, validated_data):
        image_url = validated_data.pop('image')['url']
        image = CardImage.objects.get(url=image_url)
        return Card.objects.create(image=image, **validated_data)

    def update(self, card, validated_data):
        card.cost = validated_data.get('cost', card.cost)
        card.is_available = validated_data.get('is_available', card.is_available)
        card.name = validated_data.get('name', card.name)
        image = validated_data.get('image', None)
        if image:
            image_url = image['url']
            image = CardImage.objects.get(url=image_url)
            card.image = image
        card.save()
        return card


class ImageSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CardImage
