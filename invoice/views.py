from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from invoice.models import Invoice
from invoice.serializers import InvoiceSerializer


# Create your views here.

@api_view(["GET", "POST"])
def invoice(request):
    if request.method == "GET":
        all_invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(all_invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        return Response("lkdjflakdjf")
