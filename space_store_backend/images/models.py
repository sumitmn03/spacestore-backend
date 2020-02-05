from django.db import models
from products.models import Product


class Image(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_images')
    # 1. back side 2. left side 3. right side 4. extra 5. extra
    position = models.IntegerField()
    image = models.ImageField(upload_to='images/product/')

    def __str__(self):
        return "{} image of product {}".format(str(self.position), str(self.product))
