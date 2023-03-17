# Generated by Django 4.1.7 on 2023-03-17 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0003_application_photo_service_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="description",
            field=models.TextField(default="description", max_length=10000),
        ),
        migrations.AddField(
            model_name="service",
            name="description",
            field=models.TextField(default="description", max_length=10000),
        ),
    ]
