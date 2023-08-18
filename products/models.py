from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,
                               verbose_name="Главная категория", blank=True, null=True)
    name = models.CharField(verbose_name="Имя", max_length=255)
    image = models.ImageField(upload_to='Category_images')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Имя продукта", max_length=255)
    description = models.TextField(verbose_name="О продукте")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество продкта", default=0)
    image = models.ImageField(upload_to="Product_images", blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
