from django.db import models

from cards.models import Card, PaperType
from pins.models import Pin
from utils.models import Model


class Order(Model):
    contact = models.EmailField()
    destination = models.TextField()

    @property
    def cost(self):
        cost = 0
        for pin in self.pins.all():
            cost += pin.cost
        for card in self.custom_cards.all():
            cost += card.cost
        return cost


class CardOrder(Model):
    card = models.ForeignKey(Card, default=None, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order,
                              blank=True,
                              default=None,
                              null=True,
                              on_delete=models.PROTECT,
                              related_name='cards')
    paper = models.ForeignKey(PaperType, on_delete=models.PROTECT, default=1)


class PinOrder(Model):
    pin = models.ForeignKey(Pin, default=None, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order,
                              blank=True,
                              default=None,
                              null=True,
                              on_delete=models.PROTECT,
                              related_name='pins')


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
