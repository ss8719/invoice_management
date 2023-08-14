from django.urls import path

from invoice.views import invoice, invoice_details

urlpatterns = [
    path('', invoice, name=""),
    path('detail/', invoice_details, name="invoice_details"),
]
