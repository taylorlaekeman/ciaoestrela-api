from rest_framework import serializers

from custom_cards.models import CustomCard
from .models import Order, Payment


class OrderSerializer(serializers.ModelSerializer):
    cost = serializers.DecimalField(decimal_places=2, max_digits=8, read_only=True)
    custom_cards = serializers.PrimaryKeyRelatedField(allow_null=True, many=True, queryset=CustomCard.objects.all())

    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order']
