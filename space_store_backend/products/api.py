from rest_framework import viewsets, permissions
from products.models import (
    Product,
    EditableProduct,
    HomeEditableProduct
)
from .serializers import (
    ProductSerializer,
    EditableProductSerializer,
    HomeEditableProductSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class EditableProductViewSet(viewsets.ModelViewSet):
    queryset = EditableProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EditableProductSerializer


class HomeEditableProductViewSet(viewsets.ModelViewSet):
    queryset = HomeEditableProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HomeEditableProductSerializer
