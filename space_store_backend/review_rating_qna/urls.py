from django.urls import path
from .api import ReviewViewSet, QnaViewSet

urlpatterns = [
    path('api/mainproductreview', ReviewViewSet.as_view()),
    path('api/mainproductqna', QnaViewSet.as_view()),
]
