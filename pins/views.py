import logging
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .image_client import ImageClient
from .models import Image, Pin
from .serializers import ImageSerializer, PinSerializer


logger = logging.getLogger(__name__)


class PinViewset(ModelViewSet):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    http_method_names = ['get', 'patch', 'post']

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


class ImageViewset(ModelViewSet):
    http_method_names = ['post']
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def create(self, request):
        client = ImageClient()
        image = Image()
        image.save()
        url = client.upload('pins/{}.png'.format(image.id), request.data['file'])
        image.url = url
        image.save()
        return Response(ImageSerializer(image).data)
