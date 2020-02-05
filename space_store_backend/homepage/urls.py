from rest_framework import routers
from .api import HomepageViewSet

router = routers.DefaultRouter()

router.register('api/homepage', HomepageViewSet, 'homepage'),

urlpatterns = router.urls
