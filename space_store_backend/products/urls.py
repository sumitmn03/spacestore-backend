from rest_framework import routers
from django.urls import path

from .api import (
    ProductViewSet,
    EditableProductViewSet,
    SearchViewset,
    ProductReviewViewSet,
    ProductQnaViewSet
)

router = routers.DefaultRouter()

router.register('api/products',
                ProductViewSet, 'product')
router.register('api/editableproducts',
                EditableProductViewSet, 'editable_products')
router.register('api/getproductreview',
                ProductReviewViewSet, 'getproductreview'),
router.register('api/getproductqna',
                ProductQnaViewSet, 'getproductqna')

urlpatterns = [
    path('api/searchproducts/<str:order_by>/<str:search>/<str:type>/<str:color>/<str:design_type>/<str:size>/',
         SearchViewset.as_view(), name='search'),

]

urlpatterns += router.urls
