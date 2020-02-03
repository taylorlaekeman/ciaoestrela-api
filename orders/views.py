from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order, OrderType
from .serializers import OrderSerializer, OrderTypeSerializer


class OrderViewset(viewsets.ViewSet):
    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.initial_data)


class OrderTypeViewset(viewsets.ModelViewSet):
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer
