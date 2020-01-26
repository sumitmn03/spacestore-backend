from rest_framework import routers
from .api import (
    ProductViewSet,
    EditableProductViewSet,
    HomeEditableProductViewSet
)

router = routers.DefaultRouter()

router.register('api/products', ProductViewSet, 'products')
router.register('api/editableproducts',
                EditableProductViewSet, 'editable_products')
router.register('api/homeeditableproducts',
                HomeEditableProductViewSet, 'home_editable_products')

urlpatterns = router.urls
