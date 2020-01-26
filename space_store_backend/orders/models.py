from django.db import models
from products.models import Product
from addresses.models import Address
from django.contrib.auth import get_user_model
User = get_user_model()


class Order(models.Model):
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders', default=62)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    order_datetime = models.DateTimeField(auto_now_add=True)
    # delivery status - 1. Waiting for approval 2. Approved 3. Shipped. 4. Out for delivery 5. Out of delivery 6. Delivered 7. Picked up 8. Confirmed by the seller 9. Returned
    delivery_status = models.CharField(max_length=15, default="Delivered")
    delivery_datetime = models.DateTimeField(auto_now=True)
    shipping_charges = models.IntegerField(default=0)
    offer_applied = models.IntegerField(default=0)

    def __str__(self):
        return "{} purchased {} on {}".format(str(self.current_user), str(self.product), str(self.order_date))
