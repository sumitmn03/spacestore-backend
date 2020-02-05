from django.contrib import admin
from .models import (
    Product,
    EditableProduct,
)

admin.site.register(Product)
admin.site.register(EditableProduct)
