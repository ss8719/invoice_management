# Generated by Django 4.2.4 on 2023-08-14 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("invoice", "0006_delete_book"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoicedetail",
            name="invoice_number",
            field=models.OneToOneField(
                editable=False,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invoice_detail",
                to="invoice.invoice",
            ),
        ),
    ]
