# Generated by Django 3.2.23 on 2023-12-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_product_b_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='b_stock',
            field=models.BooleanField(default=False),
        ),
    ]
