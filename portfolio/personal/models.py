
from django.db import models

# Modelo de la aplicación

class Estudios(models.Model):
    titulo = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    anio = models.CharField(max_length=10)
    degree = models.CharField(max_length=20)

class Habilidades(models.Model):
    nombreHabilidad = models.CharField(max_length=50)
    nivel = models.IntegerField()

class Proyectos(models.Model):
    nombreproyecto = models.CharField(max_length=50)
    fechaproyecto = models.CharField(max_length=10)
    descripcionproyecto = models.CharField(max_length=300)
    proyectoimg = models.CharField(max_length=15)

class ContactoCoworking(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    mensaje = models.TextField(max_length=300)

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)
    mensaje = models.CharField(max_length=300)

class Experiencia(models.Model):
    nombre = models.CharField(max_length=50)
    inicio = models.CharField(max_length=10)
    fin = models.CharField(max_length=10)
    empresa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)