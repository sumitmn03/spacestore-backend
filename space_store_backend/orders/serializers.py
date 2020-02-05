from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order
from products.serializers import ProductSerializer
from addresses.serializers import AddressSerializer


class OrderSerializer(ModelSerializer):
    order_date = SerializerMethodField()
    delivery_date = SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = Order
        fields = ['id', 'product', 'order_date',
                  'delivery_status', 'delivery_date']

    def get_order_date(self, obj):
        return obj.order_datetime.date()

    def get_delivery_date(self, obj):
        return obj.delivery_datetime.date()


class OrderDetailSerializer(ModelSerializer):
    product = ProductSerializer()
    address = AddressSerializer()
    order_date = SerializerMethodField()
    delivery_date = SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'product', 'address', 'order_date',
                  'delivery_status', 'delivery_date', 'shipping_charges', 'offer_applied']

    def get_order_date(self, obj):
        return obj.order_datetime.date()

    def get_delivery_date(self, obj):
        return obj.delivery_datetime.date()
