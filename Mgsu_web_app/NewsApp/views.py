from django.shortcuts import render
from django.views.generic import(ListView, DetailView,)

# Create your views here.

from .models import New

class NewListView(ListView):
    model = New
    queryset = New.objects.all().order_by("-date_created")
    #context_object_name = 'news'
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        # Добавление фотографий в контекст
        #return context
    

class NewDetailView(DetailView):
    model = New
