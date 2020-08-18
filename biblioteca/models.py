from django.db import models
from django.urls import reverse

# Create your models here.

class Materiale(models.Model):
    tipoMaterial = models.CharField(max_length = 20)
    codigo = models.CharField(max_length = 20)
    autor = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 100)
    anio = models.DateField()

    def __str__(self):
        return str(self.titulo)

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 20)
    idd = models.CharField(max_length = 20)
    fechaSalida= models.CharField(max_length = 20)
    fechaRegreso = models.CharField(max_length = 20)


class Personia(models.Model):
    tipoPersona = models.CharField(max_length = 20)
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    correo = models.CharField(max_length = 21)
    telefono = models.CharField(max_length = 20)
    numLibros = models.CharField(max_length = 20)
    aduedo = models.CharField(max_length = 20)

class Libro(models.Model):
    editorial = models.CharField(max_length = 20)


class Alumno(models.Model):
    matricula = models.CharField(max_length = 20)

class Profesore(models.Model):
    numEmpleado = models.CharField(max_length = 20)