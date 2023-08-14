# Generated by Django 4.2.4 on 2023-08-11 22:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("book", "0008_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_as_author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
