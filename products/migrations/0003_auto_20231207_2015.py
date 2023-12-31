# Generated by Django 3.2.23 on 2023-12-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20231124_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='previous_price',
            new_name='sale_price',
        ),
        migrations.AddField(
            model_name='product',
            name='b_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
    ]
