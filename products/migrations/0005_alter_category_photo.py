# Generated by Django 4.1.7 on 2023-03-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_category_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/category-picture"
            ),
        ),
    ]