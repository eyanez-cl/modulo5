from django.shortcuts import render
import random

# Create your views here.

def inicio(request):
    n = random.randint(0,100)
    context= {'variable': n}
    return render(request,'app_principal/index.html',context)
