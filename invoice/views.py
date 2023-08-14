from django.shortcuts import render
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["GET", "POST"])
def invoice(request):
    if request.method == "GET":
        return render(request, "invoice.html")
    elif request.method == "POST":
        return render(request, "invoice.html")
