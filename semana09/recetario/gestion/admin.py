from django.contrib import admin
from .models import Ingredientes, Preparacion, Receta

# Register your models here.

@admin.register(Ingredientes)
class IngredienteAdmin(admin.ModelAdmin):
    readonly_fields = ["id"] 

    list_display = ["id", "descripcion", "cantidad", "recetaId"] #Para poder decile que columnas puevo ver

    #Opciones de filtro en la barra lateral utilizando

    #Si se quiere buscar por la receta por el FK osea el recetaId no permite
    #entonces para poder buscar se debe poner primero el nombre y luego la columna
    search_fields = ["descripcion", "recetaId__titulo"]

    #editar
    list_editable = ["recetaId"]

    #Modifica el ordenamiento predeterminado o indicado en el modelo en el panel admin
    ordering = ["descripcion"]


    pass

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    #Que columnas puedo visualizar en la lista utilizo
    list_display = ["id", "titulo", "descripcion", "habilitado"] #Para poder decile que columnas puevo ver

    #Opciones de filtro en la barra lateral utilizando
    list_filter = ["habilitado"]

    #Opciones que puedo buscar
    search_fields = ["titulo", "descripcion"]

    #editar
    list_editable = ["habilitado"]

    #Modifica el ordenamiento predeterminado o indicado en el modelo en el panel admin
    ordering = ["-titulo"]

    #bloquea la edicion y creacion de determinados campos osea no nos deja crear el campos sale inhabilitado
    #readonly_fields = ["titulo"] 


@admin.register(Preparacion)
class PreparacionAdmin(admin.ModelAdmin):
    pass 
