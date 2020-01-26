from rest_framework import viewsets, permissions
from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return self.request.user.wishlist_items.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
