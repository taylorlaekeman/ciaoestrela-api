from rest_framework.viewsets import ModelViewSet

from .models import CustomCard, PaperType
from .serializers import CustomCardSerializer, PaperTypeSerializer


class CustomCardViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CustomCardSerializer
    queryset = CustomCard.objects.all()


class PaperTypeViewSet(ModelViewSet):
    queryset = PaperType.objects.all()
    serializer_class = PaperTypeSerializer
