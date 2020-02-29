from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from orders.views import OrderViewset, OrderTypeViewset, PaperTypeViewset, PaymentViewset


router = routers.DefaultRouter()
router.register(r'orders', OrderViewset, basename='orders')
router.register(r'order-types', OrderTypeViewset)
router.register(r'paper-types', PaperTypeViewset)
router.register(r'payments', PaymentViewset, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
