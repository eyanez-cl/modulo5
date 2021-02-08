import random
from django.shortcuts import render

# Create your views here.
def principal(request):
    context={'temperatura': random.randint(10,32),
             'humedad': random.randint(0,101),
             'ph': random.randint(1,8),
             'presion': random.randint(2,50),
             'maldad': random.randint(1,11)}
    return render(request,'app2/index.html', context)