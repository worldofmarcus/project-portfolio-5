# Generated by Django 4.1.2 on 2022-10-28 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_date_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='date_created_on',
            new_name='date_created',
        ),
    ]
