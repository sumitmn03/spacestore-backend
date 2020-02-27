# import os
# from django.http import HttpResponse
# from wsgiref.util import FileWrapper
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Order, ParentOrder, ReturnReason
from .serializers import OrderSerializer, PostOrderSerializer, ParentOrderSerializer, ReturnReasonSerializer

from accounts.serializers import UserSerializer
from addresses.models import Address

from django.contrib.auth import get_user_model
User = get_user_model()

# this is used to get order data


class OrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all().order_by('-order_datetime')

# this is used for the parent order


class ParentOrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ParentOrderSerializer

    def get_queryset(self):
        return self.request.user.parent_orders.all()


# this is used to post order datas
class PostOrderViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostOrderSerializer

    def get_queryset(self):
        return self.request.user.orders.all()

    # used to create multiple objects and i got this from https://stackoverflow.com/questions/14666199/how-do-i-create-multiple-model-instances-with-django-rest-framework
    def create(self, request, *args, **kwargs):
        current_user = request.data[0]['current_user']
        current_user_obj = User.objects.get(id=current_user)

        address = request.data[0]['address']
        address_obj = Address.objects.get(id=address)

        self.parent_order = ParentOrder.objects.create(
            current_user=current_user_obj, address=address_obj)

        # now saving the children order
        serializer = self.get_serializer(
            data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user,
                        parent_order=self.parent_order)


class ReturnReasonViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ReturnReasonSerializer

    def get_queryset(self):
        return ReturnReason.objects.all()


# def pdf_download(request, filename):
#     path = os.expanduser('~/space_store_backend/media/invoices/')
#     f = open(path+filename, "r")
#     response = HttpResponse(FileWrapper(f), content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=resume.pdf'
#     f.close()
#     return response
