# Generated by Django 4.1.7 on 2023-03-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0004_application_description_service_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stuff",
            name="profile_photo",
            field=models.ImageField(
                default="media/ima.png", upload_to="media/profile-photos"
            ),
        ),
    ]