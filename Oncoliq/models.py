from django.db import models

# Create your models here.

class Laboratorio(models.Model):
    laboratorio = models.CharField(max_length=30)
    operario = models.CharField(max_length=30)
    email = models.EmailField()
    equipo = models.CharField(max_length=30)
    fecha = models.DateField()
    resultado = models.CharField(max_length=30)

class Medico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.EmailField()
    institucion = models.CharField(max_length=30)
    informe = models.CharField(max_length=200)
    mamografia = models.CharField(max_length=30)

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()