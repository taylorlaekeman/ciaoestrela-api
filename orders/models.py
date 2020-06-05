import logging
from django.db import models
from utils.models import Model

from pins.models import Pin

logger = logging.getLogger(__name__)


class Order(models.Model):
    contact = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    destination = models.TextField()
    modified_date = models.DateTimeField(auto_now=True)
    pins = models.ManyToManyField(Pin, blank=True, default=None)

    @property
    def cost(self):
        cost = 0
        for pin in self.pins.all():
            cost += pin.cost
        for card in self.custom_cards.all():
            cost += card.cost
        return cost


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
