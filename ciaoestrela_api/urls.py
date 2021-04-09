from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cards.views import ImageViewSet as CardImageViewSet, CardViewSet
from custom_cards.views import CustomCardViewSet, PaperTypeViewSet
from orders.views import OrderViewSet, PaymentViewSet
from pins.views import ImageViewset as PinImageViewset, PinViewset


router = routers.DefaultRouter()
router.register(r'cards', CardViewSet)
router.register(r'card-images', CardImageViewSet)
router.register(r'custom-cards', CustomCardViewSet)
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'paper-types', PaperTypeViewSet)
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'pins', PinViewset)
router.register(r'pin-images', PinImageViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
