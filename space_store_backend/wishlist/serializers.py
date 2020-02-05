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

    def create(self, validated_data):
        current_user = validated_data.get('current_user')
        product = validated_data.get('product')
        if Wishlist.objects.filter(current_user=current_user, product=product).exists():
            obj = Wishlist.objects.get(
                current_user=current_user, product=product)
            return obj
        else:
            return Wishlist.objects.create(**validated_data)
