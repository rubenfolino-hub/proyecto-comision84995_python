
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar-autor/', views.agregar_autor, name='autor_form'),
    path('agregar-libro/', views.agregar_libro, name='libro_form'), # Nueva
    path('agregar-socio/', views.agregar_socio, name='socio_form'), # Nueva
    path('buscar/', views.buscar_libro, name='buscar_libro'),
]