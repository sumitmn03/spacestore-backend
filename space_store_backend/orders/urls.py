from rest_framework import routers
# from django.urls import path

from .api import OrderViewSet, PostOrderViewSet, ParentOrderViewSet, ReturnReasonViewSet

router = routers.DefaultRouter()

# this is used to get order data
router.register('api/orders', OrderViewSet, 'orders'),
router.register('api/post_order', PostOrderViewSet, 'post_order'),
router.register('api/parent_orders', ParentOrderViewSet, 'parent_orders'),
router.register('api/return_reason', ReturnReasonViewSet, 'return_reason'),


urlpatterns = router.urls

# urlpatterns += [
#     path('api/searchproducts/',
#          SearchViewset.as_view(), name='search'),
# ]
