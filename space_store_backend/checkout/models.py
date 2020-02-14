from django.db import models
from products.models import Product
from addresses.models import Address
from django.contrib.auth import get_user_model
User = get_user_model()


class Checkout(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='checkout_datas')
    cart_or_single = models.CharField(max_length=6, null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, related_name='checkout_datas', null=True, blank=True)
    size = models.CharField(max_length=7, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    address = models.OneToOneField(
        Address, on_delete=models.SET_NULL, related_name='checkout_datas', null=True, blank=True)
    payment_mode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return "{}'s checkout".format(str(self.user))
