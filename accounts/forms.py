

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Informe un email válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password") # Aquí aseguras los 3 campos pedidos

        