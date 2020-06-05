from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .email_client import send_confirmation_email
from .models import Order, Payment
from .payment_client import build_token
from .serializers import OrderSerializer, PaymentSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post']

    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return []

    def create(self, request):
        request.data.setdefault('custom_cards', [])
        response = super().create(request)
        response.data['payment'] = build_token(float(response.data['cost']))
        return response


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    http_method_names = ['post']

    def create(self, request):
        order_id = request.data['order']
        send_confirmation_email(order_id)
        return super().create(request)
