

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autor_form/', views.agregar_autor, name='autor_form'),
    path('libro_form/', views.agregar_libro, name='libro_form'),
    path('socio_form/', views.agregar_socio, name='socio_form'),
    
    path('editar_autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    path('editar_socio/<int:id>/', views.editar_socio, name='editar_socio'),
    
    path('borrar_autor/<int:id>/', views.borrar_autor, name='borrar_autor'),
    path('borrar_libro/<int:id>/', views.borrar_libro, name='borrar_libro'),
    path('borrar_socio/<int:id>/', views.borrar_socio, name='borrar_socio'),
    
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('about/', views.about, name='about'),
    path('gestion/', views.gestion, name='gestion'),
    
    path('perfil/', views.ver_perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
    path('login/', auth_views.LoginView.as_view(template_name='biblioteca/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'), 
]

