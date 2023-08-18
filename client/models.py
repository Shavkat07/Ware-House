from users.models import User
from django.db import models


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Order(models.Model):
    ORDER_STATUS = (
        ("created", "Yaratilgan"),
        ("accepted", "Tasdiqlangan"),
        ("completed", "Tugallangan"),
        ("canceled", 'Rad etilgan'),
    )
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name="Mahsulot Holati", max_length=34, choices=ORDER_STATUS)
    total = models.IntegerField()

    def __str__(self):
        return self.created.strftime("%d-%m-%Y")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    product_item = models.ForeignKey('products.Products', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Narxi", max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Soni", default=0)

    def __str__(self):
        return self.product_item.name

    class Meta:
        verbose_name = "Zakaz birligi"
        verbose_name_plural = "Zakaz birliklari"
