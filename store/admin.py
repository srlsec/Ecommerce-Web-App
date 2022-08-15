from django.contrib import admin
from .models import *


admin.site.register(
    [Customer, Category, Brand, Product, ProductImage, Order, OrderItem, ShippingAddress])
