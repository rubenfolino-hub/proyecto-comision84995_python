

from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Autenticación Básica
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # Perfil de Usuario
    path('perfil/', views.ver_perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    
    # Cambio de Contraseña (Requisito Especial)
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        success_url=reverse_lazy('password_success') # Asegura la redirección correcta
    ), name='cambiar_password'),
    
    path('password_success/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_success.html'
    ), name='password_success'),
]