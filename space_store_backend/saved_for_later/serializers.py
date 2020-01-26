from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import SavedForLater
from products.serializers import ProductSerializer


class SavedForLaterSerializer(ModelSerializer):
    sfl_product = SerializerMethodField()

    class Meta:
        model = SavedForLater
        fields = ['id', 'product', 'sfl_product']

    def get_sfl_product(self, obj):
        return ProductSerializer(obj.product).data
