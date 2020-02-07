from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('accounts.urls')),
    path('', include('products.urls')),
    path('', include('orders.urls')),
    path('', include('cart.urls')),
    path('', include('saved_for_later.urls')),
    path('', include('wishlist.urls')),
    path('', include('addresses.urls')),
    path('', include('my_otp.urls')),
    path('', include('review_rating_qna.urls')),
    path('', include('homepage.urls')),
    path('', include('checkout.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
