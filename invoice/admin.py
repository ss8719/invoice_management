# Register your models here.
from django.contrib import admin

from invoice.models import Invoice, InvoiceDetail

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
