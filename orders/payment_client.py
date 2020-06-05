from django.conf import settings
import stripe


def build_token(cost):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(amount=int(cost * 100), currency='cad')
    return intent.client_secret
