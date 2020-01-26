from rest_framework import viewsets, permissions
from .models import SavedForLater
from .serializers import SavedForLaterSerializer


class SavedForLaterViewSet(viewsets.ModelViewSet):

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SavedForLaterSerializer

    def get_queryset(self):
        return self.request.user.saved_for_later_items.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(current_user=self.request.user)
