import logging
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import OrderType, PaperType, Payment
from .serializers import OrderSerializer, OrderTypeSerializer, PaperTypeSerializer, PaymentSerializer
from .utils.email import send_confirmation_email
from .utils.stripe import build_payment_intent

logger = logging.getLogger(__name__)


class OrderViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            logger.warning('order is invalid %s', serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        order = serializer.save()
        intent = build_payment_intent(order.id)
        serializer.initial_data['payment'] = intent.client_secret
        serializer.initial_data['id'] = order.id
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
