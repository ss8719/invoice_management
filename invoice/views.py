from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from invoice.models import Invoice, InvoiceDetail
from invoice.serializers import InvoiceSerializer, InvoiceDetailSerializer


# Create your views here.

@api_view(["GET", "POST"])
def invoice(request):
    if request.method == "GET":
        all_invoices = Invoice.objects.prefetch_related("invoice_detail").all()
        serializer = InvoiceSerializer(all_invoices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def invoice_details(request):
    if request.method == "GET":
        all_invoice_details = InvoiceDetail.objects.all()
        serializer = InvoiceDetailSerializer(all_invoice_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
