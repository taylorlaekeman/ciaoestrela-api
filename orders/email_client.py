from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives
from django.template import loader

from .models import Order


EMAIL_TEXT = """
Hi!

I'm Alicia, the owner, operator, and artist at Ciao, Estrela Co.  Thank you so much for your order!

I'll get to work right away, and send you my rough work (for your approval) within two business days.  If you need to get in contact with me, please feel free to respond to this email!

Talk to you soon!

xx Alicia
Ciao, Estrela co.
"""


def send_confirmation_email(order_id):
    order = Order.objects.get(id=order_id)
    email_html = build_email_html(order)
    with get_connection() as connection:
        email = EmailMultiAlternatives(
            'I received your order!',
            EMAIL_TEXT,
            settings.EMAIL_USER,
            [order.contact],
            [settings.EMAIL_USER],
            connection=connection,
        )
        email.attach_alternative(email_html, 'text/html')
        email.send()


def build_email_html(order):
    return loader.render_to_string(
        'orders/templates/email.html',
        context={'destination': order.destination, 'custom_cards': order.custom_cards.all(), 'pins': order.pins.all()},
    )
