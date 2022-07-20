from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='', null=True)
    
    
class Resena(models.Model):
    idvehiculo = models.IntegerField()
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=30)


class Repuesto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)

    
    
    
class Accesorio(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='', null=True)
    

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    
    
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/avatar/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Avatares"