from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class Wishlist(models.Model):
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wishlist_items', default=62)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='wishlist_items')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} added {} in his wishlist".format(str(self.current_user), str(self.product))
