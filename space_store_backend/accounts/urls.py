from django.urls import path, include
from knox import views as knox_views
from .api import UserAPI, RegisterAPI, PWLoginAPI, OTPLoginAPI, UserProfileAPI, UserUpdateAPI

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/pwlogin', PWLoginAPI.as_view()),
    path('api/auth/otplogin', OTPLoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/userprofile', UserProfileAPI.as_view()),
    path('api/auth/userupdate', UserUpdateAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
