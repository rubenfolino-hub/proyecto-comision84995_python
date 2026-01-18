

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('agregar-autor/', views.agregar_autor, name='autor_form'), 
    path('agregar-libro/', views.agregar_libro, name='libro_form'),
    path('agregar-socio/', views.agregar_socio, name='socio_form'),
    path('buscar-libro/', views.buscar_libro, name='buscar_libro'),
    path('about/', views.about, name='about'),
]

