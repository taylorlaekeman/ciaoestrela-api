from django.conf import settings
import stripe

from .order_info import get_order_info


def build_payment_intent(order_id):
    order_info = get_order_info(order_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    return stripe.PaymentIntent.create(amount=int(order_info['cost'] * 100), currency='cad')
