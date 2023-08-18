from django.contrib import admin
from .models import Provider, Income, IncomeItem


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    pass


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('provider', 'income_date')


@admin.register(IncomeItem)
class IncomeItemAdmin(admin.ModelAdmin):
    pass
