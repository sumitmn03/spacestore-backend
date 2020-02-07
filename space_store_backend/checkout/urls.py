from rest_framework import routers
from .api import CheckoutViewSet

router = routers.DefaultRouter()

router.register('api/checkout', CheckoutViewSet, 'checkout')

urlpatterns = router.urls
