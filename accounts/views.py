

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User # <--- Agregamos esto
from django import forms # <--- Agregamos esto
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from biblioteca.models import Perfil 
from biblioteca.forms import UserEditForm, PerfilEditForm 

# --- Definimos el Formulario de Registro con Email (Requisito Profe) ---
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email") # La contraseña la maneja UserCreationForm automáticamente

# --- Vistas ---

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST) # Ahora sí está definido
        if form.is_valid():
            user = form.save()
            # Crear perfil automáticamente para el nuevo usuario
            Perfil.objects.create(user=user)
            messages.success(request, f'¡Cuenta creada para {user.username}! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})

@login_required
def ver_perfil(request):
    # Usamos get_or_create por seguridad si el perfil no se creó en el registro
    perfil_extra, created = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {
        'usuario': request.user,
        'perfil': perfil_extra
    })

@login_required
def editar_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilEditForm(request.POST, request.FILES, instance=perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "¡Perfil actualizado con éxito!")
            return redirect('perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilEditForm(instance=perfil)
    
    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

