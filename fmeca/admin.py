from django.contrib import admin
from fmeca.models import FMeca, EquipoFmeca


# Register your models here.
@admin.register(FMeca)
class PostAdmin(admin.ModelAdmin):
    list_display = ['ds_modo_falla', 'ds_efecto_falla', 'descripcion_tarea', 'created_at']


@admin.register(EquipoFmeca)
class EquipoFmecaAdmin(admin.ModelAdmin):
    list_display = ['equipo_id','fmeca_id', 'created_at','updated_at']