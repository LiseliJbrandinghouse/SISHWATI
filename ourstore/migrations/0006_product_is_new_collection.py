# Generated by Django 5.1 on 2024-09-21 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourstore', '0005_product_is_out_of_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new_collection',
            field=models.BooleanField(default=False),
        ),
    ]
