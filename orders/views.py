from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
import stripe

from .models import OrderType, PaperType, Payment
from .serializers import OrderSerializer, OrderTypeSerializer, PaperTypeSerializer, PaymentSerializer
from .utils.email import send_confirmation_email


class OrderViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(amount=100, currency='cad')
        serializer.initial_data['payment'] = intent.client_secret
        return Response(serializer.initial_data)


class OrderTypeViewset(viewsets.ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer


class PaperTypeViewset(viewsets.ModelViewSet):
    queryset = PaperType.objects.all()
    serializer_class = PaperTypeSerializer


class PaymentViewset(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['post']

    def create(self, request):
        response = super().create(request)
        order_id = request.data['order']
        send_confirmation_email(order_id)
        return response
