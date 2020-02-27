from rest_framework import viewsets, permissions, generics, filters
from rest_framework.response import Response
from django.db.models import Q
from products.models import (
    Product,
    EditableProduct,
)
from .serializers import (
    ProductSerializer,
    EditableProductSerializer,
    SingleProductSerializer,
    ProductReviewSerializer,
    ProductQnaSerializer
)

from .pagination import ProductsPagination

import re


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SingleProductSerializer

    def get_serializer_context(self):
        return {'user': self.request.user, 'is_anonymous': self.request.user.is_anonymous}


class SearchViewset(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    pagination_class = ProductsPagination

    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        order_by_val = self.kwargs['order_by']
        search_queries = re.findall(r"[\w']+", self.kwargs['search'])
        type_queries = re.findall(r"[\w']+", self.kwargs['type'])
        color_queries = re.findall(r"[\w']+", self.kwargs['color'])
        design_type_queries = re.findall(r"[\w']+", self.kwargs['design_type'])
        size_queries = re.findall(r"[\w']+", self.kwargs['size'])

        search_q = Q()

        for query in search_queries:
            search_q &= (Q(search_kw__icontains=query) | Q(name__icontains=query) | Q(
                product_type__icontains=query) | Q(product_color__icontains=query) | Q(product_design_type__icontains=query))

        type_q = Q()

        for query in type_queries:
            type_q |= Q(product_type__iexact=query)

        color_q = Q()

        for query in color_queries:
            color_q |= Q(product_color__iexact=query)

        design_type_q = Q()

        for query in design_type_queries:
            design_type_q |= Q(search_kw__icontains=query)

        size_q = Q()

        for query in size_queries:
            size_q |= (Q(size_n_quantity__size__iexact=query) &
                       Q(size_n_quantity__quantity__gt=0))

        final_q = (search_q) & (type_q) & (
            color_q) & (design_type_q) & (size_q)

        return Product.objects.filter(final_q).order_by(order_by_val)


class ProductReviewViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductReviewSerializer


class ProductQnaViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductQnaSerializer


class EditableProductViewSet(viewsets.ModelViewSet):
    queryset = EditableProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EditableProductSerializer
