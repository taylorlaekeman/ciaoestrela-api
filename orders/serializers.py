from rest_framework import serializers

from .models import Order, OrderType, PaperType, Payment
from .utils.create_order_item import create_order_item


class OrderItemSerializer(serializers.Serializer):
    order_type = serializers.CharField()
    ideas = serializers.CharField(required=False)


class OrderSerializer(serializers.Serializer):
    contact = serializers.EmailField()
    destination = serializers.CharField()
    items = serializers.ListField(child=OrderItemSerializer())

    def create(self, validated_data):
        order = Order.objects.create(
            contact=validated_data['contact'],
            destination=validated_data['destination'],
        )
        items = []
        for item in validated_data['items']:
            items.append(create_order_item(order, item))
        return order


class OrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderType
        fields = ['name', 'cost']


class PaperTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaperType
        fields = ['name']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['order']
