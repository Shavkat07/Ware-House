from django.contrib import admin

from .models import WareHouse, WareHouseProduct


@admin.register(WareHouse)
class WarehouseAdmin(admin.ModelAdmin):
    pass


@admin.register(WareHouseProduct)
class WarehouseProductAdmin(admin.ModelAdmin):
    pass
