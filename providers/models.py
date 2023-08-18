import datetime
from django.db import models
from products.models import Category


class Provider(models.Model):
    name = models.CharField(max_length=355)
    phone = models.CharField(max_length=16)
    info = models.TextField(verbose_name="Provider haqida malumot")

    class Meta:
        verbose_name = 'Провайдер'
        verbose_name_plural = 'Провайдеры'

    def __str__(self):
        return self.name


class Income(models.Model):
    INCOME_STATUS = (
        ("created", "Yaratilgan"),
        ("accepted", "Tasdiqlangan"),
        ("completed", "Tugallangan"),
        ("canceled", 'Rad etilgan'),
    )
    provider = models.ForeignKey(to=Provider, on_delete=models.PROTECT)
    total = models.IntegerField(verbose_name="Цена", default=0)
    status = models.CharField(verbose_name="Статус", max_length=255, choices=INCOME_STATUS)
    income_date = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    warehouse = models.ForeignKey('warehouse.Warehouse', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Импортированный товар'
        verbose_name_plural = 'Импортированные товары'

    def __str__(self):
        return self.income_date.strftime("%d-%m-%Y")

        # return f"{self.provider} kompaniyasidan {self.}"


class IncomeItem(models.Model):
    income = models.ForeignKey(to=Income, on_delete=models.PROTECT)
    product = models.ForeignKey(to=Category, on_delete=models.PROTECT)
    total_amount = models.IntegerField(verbose_name="Jami Summa", default=0)
    total_quantity = models.PositiveIntegerField(verbose_name="Jami Mahsulotlar soni", default=0)

    def __str__(self):
        return self.product.name

    # class Meta:
    #     verbose_name = ""
