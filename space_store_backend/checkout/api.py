from rest_framework import viewsets, permissions
from .models import Checkout
from .serializers import CheckoutSerializer


class CheckoutViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CheckoutSerializer

    def get_queryset(self):
        return Checkout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'user': self.request.user}
