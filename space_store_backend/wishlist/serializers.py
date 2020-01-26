from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Wishlist
from products.serializers import ProductSerializer


class WishlistSerializer(ModelSerializer):
    wishlist_product = SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = ['id', 'product', 'wishlist_product']

    def get_wishlist_product(self, obj):
        return ProductSerializer(obj.product).data
