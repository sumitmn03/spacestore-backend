from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, default="T-shirt")
    product_type = models.CharField(max_length=15, default="tshirt")
    product_color = models.CharField(max_length=15, default="white")
    product_design_type = models.CharField(max_length=30, default="plain")
    search_kw = models.TextField(null=True, blank=True)
    original_price = models.IntegerField(default=0)
    seller_discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EditableProduct(models.Model):
    # product types 0. tshirt 1. hoodie 2. sweatshirt
    product_type = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default="white")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='editable_product_images/')
    time_stamp = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.color
