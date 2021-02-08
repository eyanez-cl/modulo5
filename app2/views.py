import random
from django.shortcuts import render

# Create your views here.
def principal(request):
    lista1= [1,2,3,4,5,6,7]
    lista2= ['a','b','c','d','e','f','g']
    context={'temperatura': random.randint(10,32),
             'humedad': random.randint(0,101),
             'ph': random.randint(1,8),
             'presion': random.randint(2,50),
             'maldad': random.randint(1,11),
             'lista_numeros': lista1,
             'lista_letras':lista2}
    return render(request,'app2/index.html', context)