from django.shortcuts import render
from django.http import HttpResponse
from AppNVS.models import Familiares
from django.template import loader, Template, Context

# Create your views here.


def vista_familia(request):
    
    familia = Familiares.objects.all()

    return render(request, 'Lista_Familiares.html', {"familia": familia})