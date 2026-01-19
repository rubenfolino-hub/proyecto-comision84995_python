

from django.contrib import admin
from .models import Perfil, Autor, Libro, Socio

# Registro para el Perfil de usuario (Extensión de User)
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'pais', 'direccion')

# Configuración para Autores
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacionalidad')
    search_fields = ('nombre', 'apellido')

# Configuración para Libros (Modelo con campos específicos del Brief)
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Agregamos codigo_inventario para que el admin pueda verlo de entrada
    list_display = ('codigo_inventario', 'titulo', 'autor_nombre', 'genero', 'fecha_publicacion')
    search_fields = ('titulo', 'autor_nombre', 'codigo_inventario')
    list_filter = ('genero', 'fecha_publicacion')

# Configuración para Socio
@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'email', 'fecha_alta')
    search_fields = ('dni', 'apellido', 'nombre')
    list_filter = ('fecha_alta',)
    ordering = ('apellido',)
    