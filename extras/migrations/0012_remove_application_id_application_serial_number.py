# Generated by Django 4.1.7 on 2023-03-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0011_remove_application_serial_number_application_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="application", name="id",),
        migrations.AddField(
            model_name="application",
            name="serial_number",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]