# Generated by Django 4.1.7 on 2023-03-14 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0010_categoryfeatures_caption"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CategoryFeatures", new_name="CategoryFeature",
        ),
    ]
