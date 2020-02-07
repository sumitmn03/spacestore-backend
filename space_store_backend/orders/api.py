from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer, PostOrderSerializer

# this is used to get order data


class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all().order_by('-order_datetime')


# this is used to post order datas
class PostOrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostOrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all()

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
