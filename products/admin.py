from django.contrib import admin
from .models import Category, Products


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsItemsAdmin(admin.ModelAdmin):
    pass
