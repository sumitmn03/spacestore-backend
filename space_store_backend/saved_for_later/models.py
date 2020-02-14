from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class SavedForLater(models.Model):
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='saved_for_later_items', default=62)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=7)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} added {} in his saved for later list".format(str(self.current_user), str(self.product))
