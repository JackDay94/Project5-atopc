# Generated by Django 3.2 on 2023-03-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=6, null=True),
        ),
    ]