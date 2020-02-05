from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        current_user = validated_data.get('current_user')
        if Address.objects.filter(current_user=current_user).count() >= 10:
            return Address.objects.filter(current_user=current_user)[0]
        return Address.objects.create(**validated_data)
