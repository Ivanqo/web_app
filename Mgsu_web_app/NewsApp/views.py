from django.shortcuts import render
from django.views.generic import(ListView, DetailView,)

# Create your views here.

from .models import New

class NewListView(ListView):
    model = New
    queryset = New.objects.all().order_by("-date_created")

class NewDetailView(DetailView):
    model = New
