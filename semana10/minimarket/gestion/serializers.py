#ModelSerializer se vingula con el model y trae todas las configuraciones todas las validaciones
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from .models import Categoria, Producto

#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        # Siempre debemos colocar uno de los siguientes atributos
        #fields o exclude
        #sirve para indicar al serializar que campos vamos a utilizar para hacer la validacioion
        #fields = ["id", "nombre"]
        
        #Pero si se quiere todos los campos es:
        #fields = "__all__"
        
        #Todos los campos menos el nombre es:
        exclude = ["eliminado"] #No nos mostrara el campo eliminado


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]

class ProductoDetalleSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]
        #Podemos acceder a la informacion que esta adyacente a este modelo es decir que si ponemos 1 ingresaremos 1 nivel si le 
        #ponemos 2 ingresaremos 2 niveles (si hay)
        depth = 1

class GenerarUrlAWSSerializer(Serializer):
    # Creareos manualmente todas las columnas a validar
    contentTypeValidas = ["image/jpeg", "image/png", "application/pdf"]
    extensionesValidas = ["png", "jpg", "jpeg", "pdf"]

    fileName = serializers.CharField(trim_whitespace=True, max_length=100, required=True)

    ext = serializers.ChoiceField(choices=extensionesValidas, error_messages={
        "invalid_choice": "Ext inválida, use 'png', 'jpg', 'jpeg' o 'pdf'"
    }, required=True)

    contentType = serializers.ChoiceField(choices=contentTypeValidas, required=True)

    size = serializers.FloatField(max_value=10*1024*1024, min_value=5*1024, required=True)

    folder = serializers.CharField(required=False)