from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from utils.image_client import ImageClient
from .models import Card, CardImage
from .serializers import CardSerializer, ImageSerializer


class CardViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'post']
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update':
            return [IsAuthenticated()]
        return []

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Card.objects.all()
        return Card.objects.filter(is_available=True)


class ImageViewSet(ModelViewSet):
    http_method_names = ['post']
    queryset = CardImage.objects.all()
    serializer_class = ImageSerializer

    def get_permissions(self):
        return [IsAuthenticated()]

    def create(self, request):
        client = ImageClient()
        image = CardImage()
        image.save()
        url = client.upload('cards/{}.png'.format(image.id), request.data['file'])
        image.url = url
        image.save()
        return Response(ImageSerializer(image).data)
