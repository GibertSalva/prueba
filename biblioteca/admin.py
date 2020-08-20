from django.contrib import admin
from .models import *
# Register your models here.

class PrestamoInLine(admin.TabularInline):  # Para ver los prestamos de la persona
   model = Prestamo

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
   inlines = [PrestamoInLine, ]
   list_display = ('matricula', 'apellido',)
   search_fields = ['nombre', 'apellido', 'correo', 'telefono', 'matricula']
   fieldsets = (
      ("Persona", {
         'fields': ('nombre', 'apellido',)
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


@admin.register(Materiale)
class MaterialAdm (admin.ModelAdmin):
   list_display = ["codigo" ,"titulo", "autor"]

@admin.register(Prestamo)
class PrestamoAdm (admin.ModelAdmin):
   list_display = ["fechaSalida", "fechaRegreso"]

@admin.register(Personia)
class PersonaAdm (admin.ModelAdmin):
   list_display = ["nombres", "apellido", "telefono"]

@admin.register(Libro)
class LibroAdm(admin.ModelAdmin):
   list_display = ('titulo', 'autor',)
   list_filter = ('autor', 'anio',)
   fieldsets = (
      ("Material y Editorial", {
         'fields': ('codigo', 'autor', 'titulo', 'anio', "editorial" )
      }),
      ('Estado', {
         'fields': ('status',)
      }),
   )



