# Generated by Django 4.0.5 on 2022-06-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoper_stock_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('shoper_stock_product_id', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_extended', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_price', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_active', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_default', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_value', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_warn_level', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_sold', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_code', models.CharField(blank=True, max_length=25)),
                ('shoper_stock_ean', models.CharField(blank=True, max_length=25)),
                ('shoper_stock_weight', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_weight_type', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_availability_id', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_delivery_id', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_gfx_id', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_package', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_price_wholesale', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_price_special', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_stock_calculation_unit_id', models.IntegerField(blank=True, null=True)),
                ('shoper_stock_calculation_unit_ratio', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_stock_related_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
