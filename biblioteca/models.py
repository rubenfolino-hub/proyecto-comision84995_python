

from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Libro(models.Model):
    # REQUISITOS CUMPLIDOS:
    titulo = models.CharField(max_length=200) # 1. CharField
    autor_nombre = models.CharField(max_length=200, verbose_name="Autor") # 2. CharField
    
    # 3. Campo de imagen (Agregado)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    
    # 4. Campo de fecha
    fecha_publicacion = models.DateField()
    
    # 5. Integer con unique=True (Agregado para cumplir la consigna)
    codigo_inventario = models.IntegerField(unique=True, verbose_name="Código de Inventario")
    
    genero = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} - {self.autor_nombre}"

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True) 
    foto = models.ImageField(upload_to='socios/', null=True, blank=True)
    fecha_alta = models.DateField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni})"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200, blank=True)
    pais = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    