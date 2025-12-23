
from django import forms
from .models import Autor, Libro, Socio

class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class SocioFormulario(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'

class BuscarLibroForm(forms.Form):
    titulo = forms.CharField(max_length=100, label="Título del libro")