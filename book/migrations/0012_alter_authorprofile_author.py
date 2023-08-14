# Generated by Django 4.2.4 on 2023-08-11 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0011_alter_authorprofile_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authorprofile",
            name="author",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_profile",
                to="book.author",
            ),
        ),
    ]
