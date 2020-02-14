from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Cart
from products.serializers import NormalProductSerializer


class CartSerializer(ModelSerializer):
    cart_product = SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id','current_user', 'product', 'size', 'quantity', 'cart_product']

    def get_cart_product(self, obj):
        return NormalProductSerializer(obj.product).data
