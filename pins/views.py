from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Pin
from .serializers import PinSerializer


class PinViewset(ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    http_method_names = ['post', 'get']

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return []

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pin.objects.all()
        return Pin.objects.filter(is_available=True)

    def list(self, request):
        return super().list(self, request)
