from django.db import models
from django.urls import reverse

# Create your models here.
OPCIONES = [
        ('LI', 'Librado'),
        ('PR', 'Prestado'),
        ('AR', 'Arreglandose'),
    ]

class Materiale(models.Model):
    tipoMaterial = models.CharField(max_length = 20)
    codigo = models.CharField(max_length = 20)
    autor = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 100)
    anio = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=OPCIONES,
        default='LI',
    )

    def __str__(self):
        return str(self.titulo)

class Personia(models.Model):
    tipoPersona = models.CharField(max_length = 20)
    nombres = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    correo = models.CharField(max_length = 21)
    telefono = models.CharField(max_length = 20)
    numLibros = models.CharField(max_length = 20)
    adeudo = models.CharField(max_length = 20)

    def __str__(self):
        return "{} {}".format(self.nombres,self.apellido)

class Prestamo(models.Model):
    codigo = models.CharField(max_length = 20)
    idd = models.CharField(max_length = 20)
    fechaSalida= models.CharField(max_length = 20)
    fechaRegreso = models.CharField(max_length = 20)
    persona = models.ForeignKey("Personia",on_delete=models.CASCADE,null=False)
    material = models.ForeignKey("Materiale", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.codigo)



class Libro(Materiale):
    editorial = models.CharField(max_length = 20)
    foto = models.ImageField(max_length=100, upload_to='portadas/', blank=True)
    def __str__(self):
        return str(self.editorial)

class Revista(Materiale):
    pass

class Alumno(Personia):
    matricula = models.IntegerField()

    def __str__(self):
        return str(self.matricula)

class Profesore(Personia):
    numEmpleado = models.IntegerField()

    def __str__(self):
        return str(self.numEmpleado)