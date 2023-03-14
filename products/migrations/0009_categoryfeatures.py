# Generated by Django 4.1.7 on 2023-03-14 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_categorycertification_categoryhowtouse_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryFeatures",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("serial_number", models.IntegerField(unique=True)),
                ("photo", models.ImageField(upload_to="media/product-certifications")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.category",
                    ),
                ),
            ],
        ),
    ]