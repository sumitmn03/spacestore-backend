from rest_framework import routers
from .api import OrderViewSet, PostOrderViewSet, ParentOrderViewSet

router = routers.DefaultRouter()

# this is used to get order data
router.register('api/orders', OrderViewSet, 'orders'),
router.register('api/post_order', PostOrderViewSet, 'post_order'),
router.register('api/parent_orders', ParentOrderViewSet, 'parent_orders'),


urlpatterns = router.urls
