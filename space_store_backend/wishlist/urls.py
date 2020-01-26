from rest_framework import routers
from .api import WishlistViewSet

router = routers.DefaultRouter()

router.register('api/wishlist', WishlistViewSet, 'wishlist')

urlpatterns = router.urls
