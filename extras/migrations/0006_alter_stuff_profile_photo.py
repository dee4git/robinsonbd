# Generated by Django 4.1.7 on 2023-03-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0005_alter_stuff_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stuff",
            name="profile_photo",
            field=models.ImageField(
                default="media/img.png", upload_to="media/profile-photos"
            ),
        ),
    ]
