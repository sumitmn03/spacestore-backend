from django.db import models
from products.models import Product
from addresses.models import Address

from .utils import unique_order_id_generator
from django.db.models.signals import pre_save

from django.contrib.auth import get_user_model
User = get_user_model()


class ParentOrder(models.Model):
    order_id = models.CharField(primary_key=True, max_length=120, blank=True)
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='parent_orders', default=62)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='address_order')
    order_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ordered by {}".format(str(self.order_id), str(self.current_user))

# # to generate unique order id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=ParentOrder)


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=120, blank=True)
    parent_order = models.ForeignKey(
        ParentOrder, on_delete=models.CASCADE, related_name='children_orders', blank=True, null=True)
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', default=62)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_order')
    current_price = models.IntegerField(default=0)
    seller_discount = models.IntegerField(default=0)
    size = models.CharField(max_length=5)
    quantity = models.IntegerField(default=1)
    shipping_charges = models.IntegerField(default=0)
    # no need any value for these fields below
    # delivery status - 1. Ordered 2. Approved 3. Shipped. 4. Out for delivery 5. Out of delivery 6. Cancelled 7. Delivered 8. Return requested 9. Out for pickup 10. Out of pickup 11. Picked up 12.Shipped back 13. Received by the seller 14. Cancel Return 15. Returned
    delivery_status = models.CharField(
        max_length=25, default="Ordered")
    order_datetime = models.DateTimeField(auto_now_add=True)
    delivery_datetime = models.DateTimeField(auto_now=True)
    invoice = models.FileField(upload_to='invoices/', null=True, blank=True)

    def __str__(self):
        return "{} purchased {} on {}".format(str(self.current_user), str(self.product), str(self.order_datetime))


pre_save.connect(pre_save_create_order_id, sender=Order)


class ReturnReason(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='return_reason')
    reason = models.CharField(max_length=40, default="Order placed by mistake")
