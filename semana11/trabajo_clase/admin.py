from django.contrib import admin

# Register your models here.
from trabajo_clase.models import *

#Inline para crear Inscripciones en el curso
class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripción"
    verbose_name_plural = "Inscripciones"

# Interface de administración para el modelo Curso con inline de Inscripciones
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')
    list_filter = ('departamento', 'instructor')
    search_fields = ('titulo',)
    inlines = (InscripcionInline,)


class EntregaInLine(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name_plural = "Entregas"

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso')
    list_filter = ('curso',)
    search_fields = ('titulo',)
    inlines = (EntregaInLine,)

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)

