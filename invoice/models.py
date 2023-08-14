from django.db import models


# Create your models here.
class Invoice(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class InvoiceDetail(models.Model):
    invoice_number = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name="invoice_detail",
                                          )
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
