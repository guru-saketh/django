# Generated by Django 4.2.13 on 2024-06-13 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="receipe",
            name="receipe_owner",
        ),
    ]
