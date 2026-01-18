

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import Libro, Autor, Socio
from .forms import AutorFormulario, LibroFormulario, SocioFormulario 



def inicio(request):

    autores = Autor.objects.all()
    libros = Libro.objects.all()
    return render(request, 'biblioteca/inicio.html', {'autores': autores, 'libros': libros})

def about(request):
    usuario = {
        "nombre": "Ruben",
        "apellido": "Folino",
        "email": "ruben@coderhouse.com",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "biografia": "Hola! Soy Ruben, estudiante de Python en Coderhouse. Este proyecto es un sistema de gestión para una biblioteca desarrollado con Django",
        "cumpleanios": "18 de febrero",
    }
    return render(request, 'about.html', {'usuario': usuario})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'biblioteca/registro.html', {'form': form})



@login_required
def agregar_autor(request):
    if request.method == "POST":
        form = AutorFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorFormulario()
    return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})

@login_required
def editar_autor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        form = AutorFormulario(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = AutorFormulario(instance=autor)
    return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})

@login_required
def borrar_autor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('inicio')

@login_required
def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroFormulario()
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        form = LibroFormulario(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = LibroFormulario(instance=libro)
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

@login_required
def borrar_libro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('inicio')

@login_required
def agregar_socio(request):
    if request.method == "POST":
        form = SocioFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = SocioFormulario()
    return render(request, 'biblioteca/socio_form.html', {'miFormulario': form})

@login_required
def buscar_libro(request):
    libros = []
    query = ""
    if request.GET.get('titulo'):
        query = request.GET['titulo']
        libros = Libro.objects.filter(titulo__icontains=query)
    return render(request, 'biblioteca/buscar_libro.html', {'libros': libros, 'query': query})


@login_required
def gestion(request):
    autores = Autor.objects.all()
    libros = Libro.objects.all()
    socios = Socio.objects.all()
    return render(request, 'biblioteca/gestion.html', {
        'autores': autores, 
        'libros': libros, 
        'socios': socios
    })