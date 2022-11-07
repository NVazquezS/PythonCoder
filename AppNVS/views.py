from django.shortcuts import render
from django.http import HttpResponse
from AppNVS.models import Familiares
from django.template import loader, Template, Context

# Create your views here.


def vista_familia(request):
    
    familia = Familiares.objects.all()
    
    miHtml = open(r'D:\Curso Python\Curso CH\MVT_Nicolas_Vazquez\MVT_Nicolas_Vazquez\Templates\Lista_Familiares.html')
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    info = plantilla.render(miContexto)
    
    return HttpResponse(info )
    
    #return render(request, 'Lista_Familiares.html', {"familia": familia})