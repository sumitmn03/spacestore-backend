from rest_framework.serializers import ModelSerializer
from .models import SizeAndQuantity, ProductDetails


class SizeAndQuantitySerializer(ModelSerializer):
    class Meta:
        model = SizeAndQuantity
        fields = '__all__'


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'
