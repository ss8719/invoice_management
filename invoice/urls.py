from django.urls import path

from invoice.views import invoice

urlpatterns = [
    path('', invoice, ""),
]
