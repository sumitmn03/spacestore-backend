from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order
from products.serializers import ProductSerializer
from addresses.serializers import AddressSerializer


# this is used to get order data
class OrderSerializer(ModelSerializer):
    order_date = SerializerMethodField()
    delivery_date = SerializerMethodField()
    product = ProductSerializer()
    address = AddressSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'size', 'quantity',  'address', 'original_price', 'seller_discount', 'shipping_charges', 'delivery_status', 'order_date',
                  'delivery_date']

    def get_order_date(self, obj):
        return obj.order_datetime.date()

    def get_delivery_date(self, obj):
        return obj.delivery_datetime.date()


# this is used to post order data
class PostOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
