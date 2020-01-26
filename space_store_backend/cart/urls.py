from rest_framework import routers
from .api import CartViewSet

router = routers.DefaultRouter()

router.register('api/cart', CartViewSet, 'cart')

urlpatterns = router.urls
