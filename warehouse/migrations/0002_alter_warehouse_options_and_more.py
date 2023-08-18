# Generated by Django 4.2 on 2023-04-22 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name': 'База', 'verbose_name_plural': 'Базы'},
        ),
        migrations.AlterModelOptions(
            name='warehouseproduct',
            options={'verbose_name': 'Базовый продукт', 'verbose_name_plural': 'Базовые Продукты'},
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='warehouseproduct',
            name='total_quantity',
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='self_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=17, verbose_name='Первичная цена'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warehouseproduct',
            name='total_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество товара'),
        ),
        migrations.AlterField(
            model_name='warehouseproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.products'),
        ),
    ]
