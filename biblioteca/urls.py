

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Ruta principal
    path('', views.inicio, name='inicio'),
    
    # Rutas para crear (Create)
    path('autor_form/', views.agregar_autor, name='autor_form'),
    path('libro_form/', views.agregar_libro, name='libro_form'),
    path('socio_form/', views.agregar_socio, name='socio_form'),
    
    # Rutas para editar (Update) - Necesitan el ID del registro
    path('editar_autor/<int:id>/', views.editar_autor, name='editar_autor'),
    path('editar_libro/<int:id>/', views.editar_libro, name='editar_libro'),
    
    # Rutas para borrar (Delete) - Necesitan el ID del registro
    path('borrar_autor/<int:id>/', views.borrar_autor, name='borrar_autor'),
    path('borrar_libro/<int:id>/', views.borrar_libro, name='borrar_libro'),
    
    # Rutas de búsqueda y otros
    path('buscar_libro/', views.buscar_libro, name='buscar_libro'),
    path('about/', views.about, name='about'),
    
    # Rutas de autenticación y registro
    path('login/', auth_views.LoginView.as_view(template_name='biblioteca/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'), 
    path('gestion/', views.gestion, name='gestion'),
]
