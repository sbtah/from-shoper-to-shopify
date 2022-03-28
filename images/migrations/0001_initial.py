# Generated by Django 4.0.3 on 2022-03-28 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoper_gfx_id', models.CharField(max_length=20, unique=True)),
                ('shopify_id', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_product_id', models.CharField(blank=True, max_length=20, null=True)),
                ('shopify_product_id', models.CharField(blank=True, max_length=20, null=True)),
                ('shoper_main', models.BooleanField(default=False)),
                ('shoper_title_pl', models.CharField(blank=True, max_length=100, null=True)),
                ('shoper_title_en', models.CharField(blank=True, max_length=100, null=True)),
                ('shoper_title_de', models.CharField(blank=True, max_length=100, null=True)),
                ('shoper_title_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.CharField(blank=True, choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eighth'), ('9', 'Ninth'), ('10', 'Tenth'), ('11', 'Eleventh'), ('12', 'Twelfth'), ('13', 'Thirteenth'), ('14', 'Fourteenth'), ('15', 'Fifteenth')], max_length=2, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('shoper_link_pl', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shoper_link_en', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shoper_link_de', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shoper_link_fr', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shopify_link', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('shoper_unic', models.CharField(max_length=255, unique=True)),
                ('hidden', models.BooleanField(default=False)),
                ('extension', models.CharField(blank=True, max_length=3, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
