from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Materiale)
class Material (admin.ModelAdmin):
   list_display = ["codigo" ,"titulo", "autor"]

@admin.register(Prestamo)
class Prestamo (admin.ModelAdmin):
   list_display = ["fechaSalida", "fechaRegreso"]

@admin.register(Personia)
class Persona (admin.ModelAdmin):
   list_display = ["nombre", "apellido", "telefono"]



