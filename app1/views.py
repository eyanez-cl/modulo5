import random
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

