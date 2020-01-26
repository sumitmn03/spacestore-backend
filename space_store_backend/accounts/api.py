from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer, RegisterSerializer, LoginSerializer, UserUpdateSerializer

from my_otp.models import email_otp

from django.contrib.auth import get_user_model
User = get_user_model()


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# user update api


class UserUpdateAPI(generics.GenericAPIView):
    serializer_class = UserUpdateSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        if (email_otp.objects.filter(email=request.data["email"]).exists()):
            token = email_otp.objects.get(email=request.data["email"]).token
            if (int(token) == int(request.data["otp"]) and User.objects.filter(email=request.data["email"]).exists()):
                obj = User.objects.get(email=request.data["email"])
                serializer = self.get_serializer(obj, data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save(email=request.data["email"])

                otp_obj_of_the_email = email_otp.objects.get(
                    email=request.data["email"])
                otp_obj_of_the_email.delete()

                return Response({
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,

                })
            else:
                return Response({
                    "error": "Wrong OTP"
                })

        else:
            return Response({
                "error": "OTP for the email couldn't be found"
            })

# profile update api


class UserProfileAPI(generics.GenericAPIView):
    serializer_class = UserProfileSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, *args, **kwargs):
        if (UserProfile.objects.filter(user=self.request.user).exists()):
            obj = UserProfile.objects.get(user=self.request.user)
            serializer = self.get_serializer(obj, data=request.data)
            serializer.is_valid(raise_exception=True)
            user_profile = serializer.save(user=self.request.user)
            return Response({
                "user_profile": UserProfileSerializer(user_profile, context=self.get_serializer_context()).data
            })
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_profile = serializer.save(user=self.request.user)
            return Response({
                "user_profile": UserProfileSerializer(user_profile, context=self.get_serializer_context()).data
            })

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        if (email_otp.objects.filter(email=request.data["email"]).exists()):
            token = email_otp.objects.get(email=request.data["email"]).token
            if (int(token) == int(request.data["otp"])):
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()

                # delete otp from database as it is of no use after the user gets registered

                otp_obj_of_the_email = email_otp.objects.get(
                    email=request.data["email"])
                otp_obj_of_the_email.delete()

                return Response({
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]

                })
            else:
                return Response({
                    "error": "Wrong OTP"
                })

        else:
            return Response({
                "error": "OTP for the email couldn't be found"
            })


class PWLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class OTPLoginAPI(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        if (User.objects.filter(email=request.data["email"]).exists() and email_otp.objects.filter(email=request.data["email"]).exists()):
            token = email_otp.objects.get(email=request.data["email"]).token
            if (int(token) == int(request.data["otp"])):
                user = User.objects.get(email=request.data["email"])

                otp_obj_of_the_email = email_otp.objects.get(
                    email=request.data["email"])
                otp_obj_of_the_email.delete()

                return Response({
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]

                })
            else:
                return Response({
                    "error": "Wrong OTP"
                })

        else:
            return Response({
                "error": "OTP for the email couldn't be found"
            })
