from rest_framework import routers
from .api import SavedForLaterViewSet

router = routers.DefaultRouter()

router.register('api/savedforlater', SavedForLaterViewSet, 'savedforlater')

urlpatterns = router.urls
