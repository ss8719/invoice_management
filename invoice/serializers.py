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
        print("sameer singh")
        print(validated_data)
        validated_data["price"] = self.context["unit_price"] * self.context["quantity"]
        return InvoiceDetail.objects.create(**validated_data)
