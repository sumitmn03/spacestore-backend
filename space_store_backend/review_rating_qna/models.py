from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model
User = get_user_model()


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=30)
    rating = models.IntegerField()
    review = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name


class Q_N_A(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='q_n_as')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='q_n_as')
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product)
