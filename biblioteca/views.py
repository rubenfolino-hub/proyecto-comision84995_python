


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Libro, Autor, Socio 
from .forms import AutorFormulario, LibroFormulario, SocioFormulario 

# --- VISTAS BASADAS EN CLASES ---
class InicioView(ListView):
    model = Libro
    template_name = 'biblioteca/inicio.html'
    context_object_name = 'libros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()
        return context

class GestionView(LoginRequiredMixin, ListView):
    model = Socio
    template_name = 'biblioteca/gestion.html'
    context_object_name = 'socios' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = Autor.objects.all()
        context['libros'] = Libro.objects.all()
        return context

# --- DETALLES ---
class SocioDetalle(LoginRequiredMixin, DetailView):
    model = Socio
    template_name = 'biblioteca/socio_detalle.html'
    context_object_name = 'socio'

class AutorDetalle(LoginRequiredMixin, DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detalle.html'
    context_object_name = 'autor'

class LibroDetalle(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'biblioteca/libro_detalle.html'
    context_object_name = 'libro'

# --- ACERCA DE MÍ ---
def about(request):
    usuario = {
        "nombre": "Ruben",
        "apellido": "Folino",
        "email": "ruben@coderhouse.com",
        "avatar": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        "biografia": "Hola! Soy Ruben, estudiante de Python en Coderhouse.",
        "cumpleanios": "18 de febrero",
    }
    return render(request, 'about.html', {'usuario': usuario})

# --- BUSCADOR (CORREGIDO) ---
@login_required 
def buscar_libro(request):
    query = request.GET.get('titulo', '')
    
    if query:
        # Si hay búsqueda, filtramos
        libros = Libro.objects.filter(
            Q(titulo__icontains=query) | 
            Q(autor_nombre__icontains=query)
        ).distinct()
    else:
        # SI NO HAY BÚSQUEDA, mostramos todos los libros cargados
        libros = Libro.objects.all()
            
    return render(request, 'biblioteca/buscar_libro.html', {'libros': libros, 'query': query})

# --- GESTIÓN DE AUTORES ---
@login_required 
def agregar_autor(request):
    if request.method == "POST":
        form = AutorFormulario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor agregado con éxito")
            return redirect('gestion')
    else:
        form = AutorFormulario()
    return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})

@login_required
def editar_autor(request, id):
    try:
        autor = Autor.objects.get(id=id)
        if request.method == "POST":
            form = AutorFormulario(request.POST, instance=autor)
            if form.is_valid():
                form.save()
                messages.success(request, "Autor actualizado")
                return redirect('gestion')
        else:
            form = AutorFormulario(instance=autor)
        return render(request, 'biblioteca/autor_form.html', {'miFormulario': form})
    except Autor.DoesNotExist:
        messages.error(request, "El autor no existe")
        return redirect('gestion')

@login_required
def borrar_autor(request, id):
    Autor.objects.get(id=id).delete()
    messages.warning(request, "Autor eliminado")
    return redirect('gestion')

# --- GESTIÓN DE LIBROS ---
@login_required
def agregar_libro(request):
    if request.method == "POST":
        form = LibroFormulario(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, "Libro registrado")
            return redirect('gestion')
    else:
        form = LibroFormulario()
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

@login_required
def editar_libro(request, id):
    libro = Libro.objects.get(id=id)
    if request.method == "POST":
        form = LibroFormulario(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado")
            return redirect('gestion')
    else:
        form = LibroFormulario(instance=libro)
    return render(request, 'biblioteca/libro_form.html', {'miFormulario': form})

@login_required
def borrar_libro(request, id):
    Libro.objects.get(id=id).delete()
    messages.warning(request, "Libro eliminado")
    return redirect('gestion')

# --- GESTIÓN DE SOCIOS ---
@login_required
def agregar_socio(request):
    if request.method == "POST":
        form = SocioFormulario(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, "Socio dado de alta")
            return redirect('gestion')
    else:
        form = SocioFormulario()
    return render(request, 'biblioteca/socio_form.html', {'miFormulario': form})

@login_required
def editar_socio(request, id):
    socio = Socio.objects.get(id=id)
    if request.method == "POST":
        form = SocioFormulario(request.POST, request.FILES, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos del socio actualizados")
            return redirect('gestion')
    else:
        form = SocioFormulario(instance=socio)
    return render(request, 'biblioteca/socio_form.html', {'miFormulario': form})

@login_required
def borrar_socio(request, id):
    Socio.objects.get(id=id).delete()
    messages.warning(request, "Socio dado de baja")
    return redirect('gestion')
