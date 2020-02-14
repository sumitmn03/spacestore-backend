from rest_framework import viewsets, permissions
from .models import SavedForLater
from .serializers import SavedForLaterSerializer

from rest_framework.response import Response
from rest_framework import status


class SavedForLaterViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SavedForLaterSerializer

    def get_queryset(self):
        return self.request.user.saved_for_later_items.all().order_by('-timestamp')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data)

        if SavedForLater.objects.filter(current_user=self.request.user, product=self.request.data['product'], size=self.request.data['size']).exists():
            obj = SavedForLater.objects.get(
                current_user=self.request.user, product=self.request.data['product'], size=self.request.data['size'])
            serializer = self.get_serializer(
                obj, data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
