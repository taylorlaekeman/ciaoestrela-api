from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from custom_cards.views import CustomCardViewSet, PaperTypeViewSet
from orders.views import OrderViewset, PaymentViewset
from pins.views import ImageViewset as PinImageViewset, PinViewset


router = routers.DefaultRouter()
router.register(r'custom-cards', CustomCardViewSet)
router.register(r'orders', OrderViewset, basename='orders')
router.register(r'paper-types', PaperTypeViewSet)
router.register(r'payments', PaymentViewset, basename='payments')
router.register(r'pins', PinViewset)
router.register(r'pin-images', PinImageViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
