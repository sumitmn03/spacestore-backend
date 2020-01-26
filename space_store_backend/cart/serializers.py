from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Cart
from products.serializers import ProductSerializer


class CartSerializer(ModelSerializer):
    cart_product = SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'cart_product']

    def get_cart_product(self, obj):
        return ProductSerializer(obj.product).data
