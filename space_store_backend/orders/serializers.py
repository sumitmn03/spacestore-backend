from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order, ParentOrder, ReturnReason
from products.serializers import ProductSerializer, NormalProductSerializer
from addresses.serializers import AddressSerializer


# this is used to get order data
class OrderSerializer(ModelSerializer):
    order_date = SerializerMethodField()
    delivery_date = SerializerMethodField()
    product = NormalProductSerializer()

    class Meta:
        model = Order
        fields = ['order_id', 'parent_order', 'product', 'size', 'quantity', 'current_price',
                  'seller_discount', 'shipping_charges', 'delivery_status', 'invoice', 'order_date', 'delivery_date']

    def get_order_date(self, obj):
        return obj.order_datetime.date()

    def get_delivery_date(self, obj):
        return obj.delivery_datetime.date()


# this is used to post order data
class PostOrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class ParentOrderSerializer(ModelSerializer):
    children_orders = OrderSerializer(many=True)
    address = AddressSerializer()

    class Meta:
        model = ParentOrder
        fields = ['order_id', 'current_user', 'address',
                  'order_datetime', 'children_orders']


class ReturnReasonSerializer(ModelSerializer):
    class Meta:
        model = ReturnReason
        fields = '__all__'
