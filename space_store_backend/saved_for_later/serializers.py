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

    def create(self, validated_data):
        current_user = validated_data.get('current_user')
        product = validated_data.get('product')
        if SavedForLater.objects.filter(current_user=current_user, product=product).exists():
            obj = SavedForLater.objects.get(
                current_user=current_user, product=product)
            return obj
        else:
            return SavedForLater.objects.create(**validated_data)
