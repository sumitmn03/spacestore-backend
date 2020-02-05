from django.db import models
from products.models import Product


class Homepage(models.Model):
    category = models.CharField(max_length=25, default="Coders")
    ordering = models.IntegerField(default=0)
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="home_product")

    def __str__(self):
        return self.category
