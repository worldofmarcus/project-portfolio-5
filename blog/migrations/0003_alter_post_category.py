# Generated by Django 4.1.2 on 2022-11-08 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Releases', 'Releases'), ('Studio', 'Studio'), ('Tips', 'Tips')], default='Uncategorized', max_length=255),
        ),
    ]
