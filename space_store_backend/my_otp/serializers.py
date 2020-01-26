from rest_framework import serializers
from my_otp.models import email_otp


class EmailOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = email_otp
        fields = (
            'id',
            'email',
            'token'
        )
