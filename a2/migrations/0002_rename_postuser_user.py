# Generated by Django 4.2.4 on 2023-08-14 01:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("a2", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PostUser",
            new_name="User",
        ),
    ]
