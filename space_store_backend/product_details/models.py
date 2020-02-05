from django.db import models
from products.models import Product

# Create your models here.


class SizeAndQuantity(models.Model):
    SIZE_CHOICES = (
        ('XXXL', 'XXXL'),
        ('XXL', 'XXL'),
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS', 'XS'),
        ('XXS', 'XXS'),
        ('XXXS', 'XXXS'),
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='size_n_quantity', default=62)
    size = models.CharField(max_length=7, choices=SIZE_CHOICES, default="M")
    quantity = models.IntegerField(default=5)

    def __str__(self):
        return "{} {} of size {} available".format(self.quantity, self.product, self.size)


class ProductDetails(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_details', default=62)
    header = models.CharField(max_length=15, default="Fabric")
    value = models.CharField(max_length=50, default="Cotton blend")

    def __str__(self):
        return self.header
