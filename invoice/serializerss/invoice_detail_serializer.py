from rest_framework import serializers

from invoice.models import InvoiceDetail
from invoice.serializerss.invoice_serializer import InvoiceSerializer


class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice_number = InvoiceSerializer()

    class Meta:
        model = InvoiceDetail
        fields = "__all__"

    def create(self, validated_data):
        validated_data["price"] = validated_data["unit_price"] * validated_data["quantity"]
        return InvoiceDetail.objects.create(**validated_data)
