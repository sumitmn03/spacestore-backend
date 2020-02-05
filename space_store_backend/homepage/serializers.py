from rest_framework.serializers import ModelSerializer
from .models import Homepage

from products.serializers import NormalProductSerializer


class HomepageSerializer(ModelSerializer):
    product = NormalProductSerializer()
    class Meta:
        model = Homepage
        fields = ['category','product']
