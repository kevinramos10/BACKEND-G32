from django.db import models
from uuid import uuid4

# Create your models here.

class Categoria(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    habilitado = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        db_table = 'categorias'

class Media(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    ext = models.CharField(max_length=100, null=False)
    ruta = models.CharField(max_length=200, null=False)
    mimeType = models.CharField(db_column='mine_type', max_length=100, null=False)
    habilitado = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        db_table = 'medias'

class Producto(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    nombre = models.CharField(max_length=200, null=False)
    disponible = models.BooleanField(default=True)

    categoria = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, db_column='categoria_id')
    media = models.ForeignKey(to=Media, on_delete=models.PROTECT, db_column='media_id', null=True)

    habilitado = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        db_table = 'productos'

class Precio(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    disponible = models.BooleanField(null=False)

    Producto = models.ForeignKey(to=Producto, on_delete=models.PROTECT, db_column='producto_id')

    habilitado = models.BooleanField(default=True)
    eliminado = models.BooleanField(default=False)

    class Meta:
        db_table = 'precios'