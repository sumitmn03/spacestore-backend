from rest_framework import routers
from .api import CartViewSet, CartDeleteViewSet
from django.urls import path


router = routers.DefaultRouter()

router.register('api/cart', CartViewSet, 'cart')

urlpatterns = [
    path('api/delete_cart/<int:pk>/', CartDeleteViewSet.as_view()),
]

urlpatterns += router.urls
