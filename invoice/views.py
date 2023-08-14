from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(["GET", "POST"])
def invoice(request):
    if request.method == "GET":
        return Response("lkdjflakdjf")
    elif request.method == "POST":
        return Response("lkdjflakdjf")
