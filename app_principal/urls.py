from django.urls import path
from . import views

app_name = 'app_principal'

urlpatterns = [
    path('inicio',views.inicio, name='inicio')
]
