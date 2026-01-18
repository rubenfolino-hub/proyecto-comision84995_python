
from django.shortcuts import render, redirect
from .forms import AutorFormulario, LibroFormulario, SocioFormulario 
from .models import Libro 

def home(request):
    return render(request, 'home.html')

def about(request):
    usuario = {
        "nombre": "Ruben",
        "apellido": "Folino",
        "email": "ruben@coderhouse.com",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "biografia": "Estudiante de Python en Coderhouse",
        "cumpleanios": "18 de febrero",
    }
    return render(request, 'about.html', {'usuario': usuario})


def inicio(request):
    return render(request, 'biblioteca/inicio.html')

def agregar_autor(request):
    if request.method == "POST":
        form = AutorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorFormulario()
    return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})

def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroFormulario()
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

def agregar_socio(request):
    if request.method == "POST":
        form = SocioFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = SocioFormulario()
    return render(request, 'biblioteca/socio_form.html', {'miFormulario': form})

def buscar_libro(request):
    libros = []
    query = ""
    if request.GET.get('titulo'):
        query = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=query)
    return render(request, 'biblioteca/buscar_libro.html', {'libros': libros, 'query': query})
