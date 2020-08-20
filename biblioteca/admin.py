from django.contrib import admin
from .models import *
# Register your models here.

class PrestamoInLine(admin.TabularInline):
   model = Prestamo

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
   inlines = [PrestamoInLine, ]
   list_display = ('matricula', 'apellido',)
   search_fields = ['nombres', 'apellido', 'correo', 'telefono', 'matricula']
   fieldsets = (
      ("Persona", {
         'fields': ('nombres', 'apellido',)
      }),
      ('Contacto', {
         'fields': ('correo', 'telefono',)
      }),
      ('Alumno', {
         'fields': ('matricula',)
      }),
      ('Bibloteca', {
         'fields': ('numLibros', 'adeudo',)
      }),
   )

@admin.register(Profesore)
class ProfesorAdmin(admin.ModelAdmin):
   inlines = [PrestamoInLine, ]
   search_fields = ['nombres', 'apellido', 'correo', 'telefono', 'numEmpleado']
   fieldsets = (
      ("Persona", {
         'fields': ('nombres', 'apellido',)
      }),
      ('Contacto', {
         'fields': ('correo', 'telefono',)
      }),
      ('Empleado', {
         'fields': ('numEmpleado',)
      }),
      ('Bibloteca', {
         'fields': ('numLibros', 'adeudo',)
      }),
   )

@admin.register(Prestamo)
class PrestamoAdm (admin.ModelAdmin):
   list_display = ("fechaSalida", "fechaRegreso", "persona", "material",)

@admin.register(Libro)
class LibroAdm(admin.ModelAdmin):
   list_display = ('titulo', 'autor',)
   list_filter = ('autor', 'anio',)
   fieldsets = (
      ("Material y Editorial", {
         'fields': ('codigo', 'autor', 'titulo', 'anio', "editorial", "foto", )
      }),
      ('Estado', {
         'fields': ('status',)
      }),
   )



