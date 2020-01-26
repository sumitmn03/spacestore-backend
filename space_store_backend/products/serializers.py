from rest_framework.serializers import ModelSerializer, SerializerMethodField
from products.models import (
    Product,
    EditableProduct,
    HomeEditableProduct
)


class ProductSerializer(ModelSerializer):
    modified_rating = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'original_price', 'seller_discount',
                  'image', 'rating', 'modified_rating', 'time_stamp', 'deleted']

    def get_modified_rating(self, obj):
        rating = str(obj.rating)
        if '0' in rating:
            return float(rating[0])
        else:
            return obj.rating


class EditableProductSerializer(ModelSerializer):
    class Meta:
        model = EditableProduct
        fields = '__all__'


class HomeEditableProductSerializer(ModelSerializer):
    class Meta:
        model = HomeEditableProduct
        fields = '__all__'
