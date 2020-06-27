from django.db import models

from utils.models import Model


class CardImage(Model):
    url = models.URLField(blank=True)


class PaperType(models.Model):
    name = models.CharField(max_length=100)


class Card(Model):
    image = models.ForeignKey(CardImage, default=None, on_delete=models.PROTECT)
    cost = models.DecimalField(decimal_places=2, default=10, max_digits=6)
    is_available = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
