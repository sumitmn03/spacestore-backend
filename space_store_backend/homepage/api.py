from rest_framework import viewsets, permissions
from .models import Homepage
from .serializers import HomepageSerializer
from .pagination import HomepagePagination


class HomepageViewSet(viewsets.ModelViewSet):
    queryset = Homepage.objects.all().order_by('ordering')
    permission_classes = [
        permissions.AllowAny
    ]
    pagination_class = HomepagePagination
    serializer_class = HomepageSerializer
