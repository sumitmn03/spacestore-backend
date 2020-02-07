from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Cart
from products.serializers import NormalProductSerializer


class CartSerializer(ModelSerializer):
    cart_product = SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'cart_product']

    def get_cart_product(self, obj):
        return NormalProductSerializer(obj.product).data

    def create(self, validated_data):
        current_user = validated_data.get('current_user')
        product = validated_data.get('product')
        if Cart.objects.filter(current_user=current_user, product=product).exists():
            obj = Cart.objects.get(
                current_user=current_user, product=product)
            return obj
        else:
            return Cart.objects.create(**validated_data)
