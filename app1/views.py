import random
import csv
from django.conf import settings
from django.shortcuts import render

# Create your views here.

def primera(request):
    lista_nombres = ['Esteban','Luis','Claudia', 'Bruce Wayne']
    context ={'temperatura': random.randint(22,39),
              'nombres':lista_nombres} 
    return render(request,'app1/index.html',context)

def empresa(request):
    
    context ={'temperatura': random.randint(22,39)} 
    return render(request,'app1/empresa.html',context)

def contacto(request):
    
    context ={'temperatura': random.randint(22,39)} 
    return render(request,'app1/contacto.html',context)

def datos(request):
    filename = '/app1/data/iris.csv'
    ruta_completa_archivo= str(settings.BASE_DIR)+ filename
    with open(ruta_completa_archivo, 'r') as  archivo:
        data= csv.DictReader(archivo)
        data_lista= []
        for elemento in data:
            data_lista.append(elemento)
    context={'datos_desde_archivo':data_lista}
    return render(request,'app1/datos.html', context)

