from django.contrib import admin
from .models import (
    Product,
    EditableProduct,
    HomeEditableProduct
)

admin.site.register(Product)
admin.site.register(EditableProduct)
admin.site.register(HomeEditableProduct)
