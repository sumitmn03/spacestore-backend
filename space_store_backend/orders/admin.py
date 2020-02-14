from django.contrib import admin
from .models import Order, ParentOrder

admin.site.register(Order)
admin.site.register(ParentOrder)
