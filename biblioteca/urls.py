

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.InicioView.as_view(), name='inicio'),
    path('gestion/', views.GestionView.as_view(), name='gestion'),
    
    
    path('autor_form/', views.agregar_autor, name='autor_form'),
    path('editar_autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('borrar_autor/<int:id>/', views.borrar_autor, name='borrar_autor'),
    path('autor/<int:pk>/', views.AutorDetalle.as_view(), name='autor_detalle'),
    
    
    path('libro_form/', views.agregar_libro, name='libro_form'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('borrar_libro/<int:id>/', views.borrar_libro, name='borrar_libro'),
    path('libro/<int:pk>/', views.LibroDetalle.as_view(), name='libro_detalle'),
    
    
    path('socio_form/', views.agregar_socio, name='socio_form'),
    path('editar_socio/<int:id>/', views.editar_socio, name='editar_socio'),
    path('borrar_socio/<int:id>/', views.borrar_socio, name='borrar_socio'),
    path('socio/<int:pk>/', views.SocioDetalle.as_view(), name='socio_detalle'),
    
    
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('about/', views.about, name='about'),
]

