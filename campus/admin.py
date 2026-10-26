from django.contrib import admin
from .models import ODS, Organizacion, Iniciativa


@admin.register(ODS)
class ODSAdmin(admin.ModelAdmin):
    list_display = ("numero", "nombre")
    search_fields = ("nombre", "descripcion")
    ordering = ("numero",)


@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "web")
    list_filter = ("tipo",)
    search_fields = ("nombre", "descripcion")


@admin.register(Iniciativa)
class IniciativaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ods", "fecha_inicio")
    list_filter = ("ods", "fecha_inicio", "organizaciones")
    search_fields = (
        "titulo",
        "descripcion",
        "ods__nombre",
        "organizaciones__nombre",
    )
    filter_horizontal = ("organizaciones",)
    date_hierarchy = "fecha_inicio"