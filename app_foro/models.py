
from django.db import models
from datetime import datetime

# Create your models here.

class publicacion(models.Model):
    usuario = models.CharField(max_length=40)
    tema_especifico = models.CharField(max_length=50)
    consulta = models.TextField() 
    fecha_de_publicacion = models.DateField(default=datetime.now())



class contacto(models.Model):
    usuario = models.CharField(max_length=40)
    email = models.EmailField()
    razon_contacto = models.TextField()
    fecha_de_contacto = models.DateField(default=datetime.now())



class sorteo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()




