from rest_framework import routers
from .api import OrderViewSet, OrderDetailViewSet

router = routers.DefaultRouter()

router.register('api/orders', OrderViewSet, 'orders'),
router.register('api/orderdetail', OrderDetailViewSet, 'order_detail')

urlpatterns = router.urls
