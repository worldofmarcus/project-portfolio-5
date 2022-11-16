# Generated by Django 4.1.2 on 2022-11-16 18:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0009_product_users_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0.0, message=None)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='users_wishlist',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
