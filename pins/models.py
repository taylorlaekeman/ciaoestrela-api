from django.db import models

from utils.models import Model


class Pin(Model):
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField
    image_url = models.CharField(max_length=100)
    is_available = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
