# Generated by Django 4.1.2 on 2022-11-11 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date']},
        ),
    ]
