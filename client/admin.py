from django.contrib import admin
from .models import Client, Order, OrderItem


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
