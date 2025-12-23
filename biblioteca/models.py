from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    dni = models.IntegerField()
