from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.shortcuts import render
from django.template import loader

from orders.models import CustomCard, Order

EMAIL_TEXT = 'Hi!\n\nI\'m Alicia, the owner, operator, and artist at Ciao, Estrela Co.  Thank you so much for your order!\n\nI\'ll get to work right away, and send you my rough work (for your approval) within two business days.  If you need to get in contact with me, please feel free to respond to this email!\n\nTalk to you soon!\n\nxx Alicia\nCiao, Estrela co.'


def send_confirmation_email(order_id):
    order_info = get_order_info(order_id)
    email_html = build_email_html(order_info)
    with get_connection() as connection:
        email = EmailMultiAlternatives(
            'I received your order!',
            EMAIL_TEXT,
            settings.EMAIL_USER,
            [order_info['contact']],
            [settings.EMAIL_USER],
            connection=connection,
        )
        email.attach_alternative(email_html, 'text/html')
        email.send()


def get_order_info(order_id):
    order = Order.objects.get(id=order_id)
    custom_cards = CustomCard.objects.filter(order_item__order__id=order_id)
    return {
        'contact': order.contact,
        'items': [{ 'ideas': card.ideas, 'paper': card.paper.name } for card in custom_cards]
    }


def build_email_html(order_info):
    return loader.render_to_string(
        'orders/templates/email.html',
        context={'items': order_info['items']},
    )
