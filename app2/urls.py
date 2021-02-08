from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('principal/',views.principal, name='principal'),
    #path('empresa/', views.empresa, name='empresa'),
    #path('contacto/',views.contacto, name='contacto'),
]
