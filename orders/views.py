from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from rest_framework.response import Response
import stripe

from .models import Order, OrderType, PaperType
from .serializers import OrderSerializer, OrderTypeSerializer, PaperTypeSerializer


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


def send_confirmation_email(body):
    message = 'Hi!\n\nI\'m Alicia, the owner, operator, and artist at Ciao, Estrela Co.  Thank you so much for your order!\n\nI\'ll get to work right away, and send you my rough work (for your approval) within two business days.  If you need to get in contact with me, please feel free to respond to this email!\n\nTalk to you soon!\n\nxx Alicia\nCiao, Estrela co.'
    html_message = build_email_html(body)
    with get_connection() as connection:
        email = EmailMultiAlternatives(
            'I received your order!',
            message,
            settings.EMAIL_USER,
            [body['contact']],
            [settings.EMAIL_USER],
            connection=connection,
        )
        email.attach_alternative(html_message, 'text/html')
        email.send()


def build_email_html(body):
    return loader.render_to_string(
        'orders/templates/email.html',
        context={'items': body['items']},
    )


class OrderTypeViewset(viewsets.ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer


class PaperTypeViewset(viewsets.ModelViewSet):
    queryset = PaperType.objects.all()
    serializer_class = PaperTypeSerializer
