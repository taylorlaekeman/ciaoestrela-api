from django.db import models

from orders.models import Order
from utils.models import Model


class PaperType(models.Model):
    name = models.CharField(max_length=100)


class CustomCard(Model):
    cost = models.DecimalField(decimal_places=2, default=10, max_digits=6)
    ideas = models.TextField(blank=True)
    order = models.ForeignKey(Order, blank=True, default=None, null=True, on_delete=models.CASCADE, related_name='custom_cards')
    paper = models.ForeignKey(PaperType, on_delete=models.PROTECT, default=1)
