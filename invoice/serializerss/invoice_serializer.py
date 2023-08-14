from rest_framework import serializers

from invoice.models import Invoice
from invoice.serializerss.invoice_detail_serializer import InvoiceDetailSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_detail = InvoiceDetailSerializer(read_only=True)

    class Meta:
        model = Invoice
        fields = "__all__"
