# Generated by Django 5.1 on 2024-09-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourstore', '0003_product_available_colors_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hover_image',
            field=models.ImageField(blank=True, null=True, upload_to='shop/'),
        ),
    ]
