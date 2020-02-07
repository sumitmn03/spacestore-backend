from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Checkout
from addresses.serializers import AddressSerializer
from products.models import Product
from products.serializers import NormalProductSerializer
from cart.models import Cart
from cart.serializers import CartSerializer


class CheckoutSerializer(serializers.ModelSerializer):
    address_data = SerializerMethodField()
    checkout_datas = SerializerMethodField()

    class Meta:
        model = Checkout
        fields = ['id', 'user', 'cart_or_single',
                  'product', 'address', 'payment_mode', 'address_data', 'checkout_datas']

    def get_address_data(self, obj):
        return AddressSerializer(obj.address).data

    def get_checkout_datas(self, obj):
        if obj.cart_or_single == "single":
            return NormalProductSerializer(Product.objects.filter(checkout_datas=obj), many=True).data
        else:
            return CartSerializer(Cart.objects.filter(current_user=self.context['user']), many=True).data
