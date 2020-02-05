from rest_framework.serializers import ModelSerializer
from .models import Review, Q_N_A


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class Q_N_ASerializer(ModelSerializer):
    class Meta:
        model = Q_N_A
        fields = '__all__'
