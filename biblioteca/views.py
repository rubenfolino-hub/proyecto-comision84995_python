
from django.shortcuts import render, redirect
from .models import Libro, Autor, Socio
from .forms import AutorFormulario, LibroFormulario, SocioFormulario, BuscarLibroForm

# Vista de Inicio
def inicio(request):
    return render(request, 'biblioteca/inicio.html')

# Vista para agregar Autores
def agregar_autor(request):
    if request.method == "POST":
        form = AutorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorFormulario()
    return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})

# Vista para agregar Libros (Esta es la que te falta)
def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroFormulario()
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

# Vista para agregar Socios (También necesaria)
def agregar_socio(request):
    if request.method == "POST":
        form = SocioFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = SocioFormulario()
    return render(request, 'biblioteca/socio_form.html', {'miFormulario': form})

# Vista de Búsqueda
def buscar_libro(request):
    libros = []
    query = ""
    if request.GET.get('titulo'):
        query = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=query)
    
    return render(request, 'biblioteca/buscar_libro.html', {'libros': libros, 'query': query})