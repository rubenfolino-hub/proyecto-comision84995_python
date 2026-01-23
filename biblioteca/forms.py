

from django import forms
from django.contrib.auth.models import User
from .models import Perfil, Autor, Libro, Socio 

class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        labels = {
            'autor_nombre': 'Nombre del Autor',
            'codigo_inventario': 'Código Único de Inventario',
            'portada': 'Imagen de Portada',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Rayuela'}),
            'autor_nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Julio Cortázar'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Novela'}),
            'codigo_inventario': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número único'}),
            'portada': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SocioFormulario(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['direccion', 'pais', 'foto']
        widgets = {
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }
        