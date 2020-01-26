from rest_framework import viewsets, permissions
from .models import Cart
from .serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.request.user.cart_items.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
