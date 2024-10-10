from django.contrib import admin
from .models import Product, Payment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'quantity')


@admin.register(Payment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'vendor', 'amount')