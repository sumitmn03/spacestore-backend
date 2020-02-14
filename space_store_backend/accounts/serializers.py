from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from django.contrib.auth import authenticate
from .models import UserProfile
from checkout.serializers import CheckoutSerializer
from checkout.models import Checkout
from django.contrib.auth import get_user_model
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'first_name', 'last_name', 'gender')


# User Serializer


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    checkout_id = SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'email', 'phone_no', 'profile', 'checkout_id')

    def get_checkout_id(self, obj):
        return obj.checkout_datas.id

# User Update Serializer


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'phone_no')


# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Checkout.objects.create(user=user)
        return user

# Login Serializer


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
