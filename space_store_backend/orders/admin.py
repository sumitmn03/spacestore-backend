from django.contrib import admin
from .models import Order, ParentOrder, ReturnReason

admin.site.register(Order)
admin.site.register(ParentOrder)
admin.site.register(ReturnReason)
