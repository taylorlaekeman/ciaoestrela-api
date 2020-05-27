from django.db import models

from utils.models import Model


class Image(Model):
    url = models.URLField(blank=True)


class Pin(Model):
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    pin_image = models.ForeignKey(Image, on_delete=models.PROTECT, default=None)
    is_available = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
