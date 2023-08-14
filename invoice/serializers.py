from rest_framework import serializers

from invoice.models import Invoice, InvoiceDetail


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = "__all__"

    def create(self, validated_data):
        validated_data["price"] = validated_data["unit_price"] * validated_data["quantity"]
        return InvoiceDetail.objects.create(**validated_data)

    def to_representation(self, instance):
        data = super(InvoiceDetailSerializer, self).to_representation(instance)
        return data


class InvoiceDetailSerializerForGet(InvoiceDetailSerializer):
    invoice = InvoiceSerializer(read_only=True)


class InvoiceSerializerWithInvoiceDetailSerializer(InvoiceSerializer):
    invoice_detail = InvoiceDetailSerializer(read_only=True)
