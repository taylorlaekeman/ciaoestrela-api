from rest_framework.serializers import ModelSerializer

from .models import CustomCard, PaperType


class CustomCardSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = CustomCard


class PaperTypeSerializer(ModelSerializer):
    class Meta:
        model = PaperType
        fields = ['name']
