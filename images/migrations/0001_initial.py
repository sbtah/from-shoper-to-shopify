# Generated by Django 4.0.5 on 2022-06-13 14:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoper_gfx_id', models.IntegerField(unique=True)),
                ('shoper_product_id', models.IntegerField(blank=True, null=True)),
                ('shoper_main', models.IntegerField(blank=True, null=True)),
                ('shoper_order', models.IntegerField(blank=True, choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth'), (9, 'Ninth'), (10, 'Tenth'), (11, 'Eleventh'), (12, 'Twelfth'), (13, 'Thirteenth'), (14, 'Fourteenth'), (15, 'Fifteenth')], null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('shoper_image_name', models.CharField(blank=True, max_length=255)),
                ('shoper_unic', models.CharField(max_length=255)),
                ('shoper_hidden', models.CharField(blank=True, max_length=1, null=True)),
                ('shoper_extension', models.CharField(blank=True, max_length=5, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('shoper_related_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='CSVImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_hard_link', models.CharField(blank=True, max_length=255)),
                ('image_position', models.IntegerField(blank=True, null=True)),
                ('shoper_related_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
        ),
    ]
