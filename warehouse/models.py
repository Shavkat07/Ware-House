from django.db import models


class WareHouse(models.Model):
    name = models.CharField(max_length=255, blank=True, )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'База'
        verbose_name_plural = 'Базы'


class WareHouseProduct(models.Model):
    warehouse = models.ForeignKey('WareHouse', on_delete=models.PROTECT)
    product = models.ForeignKey('products.Products', on_delete=models.PROTECT)
    self_price = models.DecimalField(verbose_name="Первичная цена", max_digits=17, decimal_places=2)
    total_count = models.PositiveIntegerField(verbose_name="Количество товара", default=0)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Базовый продукт'
        verbose_name_plural = 'Базовые Продукты'


