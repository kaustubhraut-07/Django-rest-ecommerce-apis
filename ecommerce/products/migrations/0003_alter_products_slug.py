# Generated by Django 5.0.7 on 2024-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_image_alter_products_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
