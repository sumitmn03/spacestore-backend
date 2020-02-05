from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Address(models.Model):
    current_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='addresses', default=62)
    name = models.CharField(max_length=100)
    # area and street
    address = models.TextField()
    # city, town
    locality = models.CharField(max_length=50)
    # landmark is optional
    landmark = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    # optional
    alt_phone = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}'s address".format(str(self.current_user))
