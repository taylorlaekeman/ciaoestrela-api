import logging
from operator import itemgetter
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CustomCard, Order, OrderItem, OrderType, PaperType, Payment
from .serializers import OrderSerializer, OrderTypeSerializer, PaperTypeSerializer, PaymentSerializer
from .utils.email import send_confirmation_email
from .utils.stripe import build_payment_intent

logger = logging.getLogger(__name__)


class OrderViewset(viewsets.ViewSet):
    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated()]
        return []

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            logger.error('order is invalid %s %s', serializer.data, serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        order = serializer.save()
        intent = build_payment_intent(order.id)
        serializer.initial_data['payment'] = intent.client_secret
        serializer.initial_data['id'] = order.id
        return Response(serializer.initial_data)

    def list(self, _):
        response = []
        payments = Payment.objects.all()
        order_indices_by_id = {}
        for index, payment in enumerate(payments):
            order = payment.order
            order_indices_by_id[order.id] = index
            response.append({
                'contact': order.contact,
                'createdDate': order.created_date,
                'destination': order.destination,
                'id': order.id,
                'items': [],
                'modifiedDate': order.modified_date
            })
        order_items = OrderItem.objects.all()
        item_indices_by_id = {}
        for item in order_items:
            order_index = order_indices_by_id.get(item.order.id, None)
            if order_index:
                order = response[order_index]
                item_indices_by_id[item.id] = len(order['items'])
                order['items'].append({
                    'type': item.order_type.name
                })
        custom_cards = CustomCard.objects.all()
        for card in custom_cards:
            order_id = card.order_item.order.id
            item_id = card.order_item.id
            order_index = order_indices_by_id.get(order_id, None)
            item_index = item_indices_by_id.get(item_id, None)
            if order_index and item_index:
                item = response[order_index]['items'][item_index]
                item['ideas'] = card.ideas
                item['paper'] = card.paper.name
        response = sorted(response, key=itemgetter('modifiedDate'), reverse=True)
        return Response(response)


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
