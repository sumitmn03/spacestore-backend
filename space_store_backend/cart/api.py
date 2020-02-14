from rest_framework import viewsets, permissions
from .models import Cart
from .serializers import CartSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CartViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.request.user.cart_items.all().order_by('-timestamp')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data)

        if Cart.objects.filter(current_user=self.request.user, product=self.request.data['product'], size=self.request.data['size']).exists():
            obj = Cart.objects.get(
                current_user=self.request.user, product=self.request.data['product'], size=self.request.data['size'])
            serializer = self.get_serializer(
                obj, data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# when order is made from cart and the order gets success, all the cart items are deleted


class CartDeleteViewSet(APIView):
    def delete(self, request, pk, format=None):
        Cart.objects.filter(current_user=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
