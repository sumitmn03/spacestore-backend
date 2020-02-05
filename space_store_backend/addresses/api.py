from rest_framework import viewsets, permissions
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = AddressSerializer

    def get_queryset(self):
        return self.request.user.addresses.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
