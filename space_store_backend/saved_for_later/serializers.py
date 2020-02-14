from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import SavedForLater
from products.serializers import NormalProductSerializer


class SavedForLaterSerializer(ModelSerializer):
    sfl_product = SerializerMethodField()

    class Meta:
        model = SavedForLater
        fields = ['id', 'product', 'quantity', 'size', 'sfl_product']

    def get_sfl_product(self, obj):
        return NormalProductSerializer(obj.product).data
