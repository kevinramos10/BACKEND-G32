from django.db import models
from uuid import uuid4

# Create your models here.
class Receta(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField()
    habilitado = models.BooleanField(default=True)

    class Meta: #Siempre se llama meta por Metatributes
        db_table = 'recetas' #Nombre de la tabla
        ordering = ['titulo'] #Ordena de la A a la Z manera ascendente
        #ordering = ['-titulo' 'descripcion'] #Ordena de la A a la A manera descendente

        #constrains sirve para poder indicar una unicidad en conjunto
        #constraints = [['titulo', 'descripcion'] ['titulo', 'habilitado']] #Sirve para que no se repita los mismo en las 2 columnas como un unique

class Ingredientes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    descripcion = models.TextField(null=False)
    cantidad = models.TextField(null=False)

    #llaves foraneas
    #on_delete y el on_update y esto se usa para las relaciones y sirve para indicar cual sera el comportamiento
    #de las llaves foraneas cuando sea eliminado o actualizado
    #CASCADE > Si el padre es eliminado, los hijos tambien sera eliminados: Si la receta se eleimina tambien se elimina todos los ingredientes de esa receta de manera automatica
    #DO_NOTHING > No hace nada y permite la eliminacion del padre y el hijo seguira conservando su id del padre: Si elimina la receta el ingrediente sigue con su id de la receta y genera la desintegirdad de datos
    #SET_DEFAULT > Se puede eliminar un valor por defecto si se elimina el padre: Si se elimina la receta se cambia por otro pacre 
    #PROTECT > Evita la eliminacion del padre si tiene hijos: Si se quiere eliminar una receta que tiene ingredientes no se podra
    #RESTRICT > Es igual que el protect solo que emite una exception de RESTRIC_VALUE_ERROR
    #SET_NULL > Permite la eliminacion del padre y chamba la eliminacion del FK a null: Si se elimina el padre los ingredientes la receta_id cambiara a null
    recetaId = models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table = 'ingredientes'

class Preparacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    descripcion = models.TextField()
    order = models.IntegerField(null=False)
    recetaId = models.ForeignKey(to=Receta, on_delete=models.PROTECT, db_column='receta_id')

    class Meta:
        db_table = 'preparaciones'
        #Unicidad en conjunto indicando que el order y la receta no se puede repetir
        # order | recetaId
        #   1   |   1
        #   2   |   1
        #   2   |   1  Esto no deja el unique

        unique_together = [['order', 'recetaId']]

