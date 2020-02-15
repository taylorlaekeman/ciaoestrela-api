from django.db import models


class OrderType(models.Model):
    name = models.CharField(max_length=100)


class Order(models.Model):
    destination = models.TextField()
    contact = models.EmailField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_type = models.ForeignKey(OrderType, on_delete=models.PROTECT)


class PaperType(models.Model):
    name = models.CharField(max_length=100)


class CustomCard(models.Model):
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    ideas = models.TextField()
    paper = models.ForeignKey(PaperType, on_delete=models.PROTECT, default=1)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, primary_key=True)
