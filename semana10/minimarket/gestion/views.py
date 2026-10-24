from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Categoria
from .serializers import CategoriaSerializer

#Nos brinnda el proceso automatico para alguna operacion
from rest_framework.generics import (CreateAPIView, #Para crear
                                    DestroyAPIView, #Eliminar
                                    ListAPIView, #devolver todo
                                    ListCreateAPIView, #Devolver todos y creacion
                                    RetrieveAPIView, #Devolver solo uno
                                    RetrieveDestroyAPIView, #Devolver solo uno y ademas eliminar
                                    RetrieveUpdateAPIView, #eliminar y ademas poder actualizar
                                    RetrieveUpdateDestroyAPIView, # devolver solo uno y ademas poder actualizarlo o eliminarlo
                                    UpdateAPIView #Actualizar


)

class CategoriasView(APIView):
    #Al usar el APIVIEW esto es muy similar al resourse de flask-restfult en el cual se puede colocar los
    #metodos http como metodos de la clase
    def get(self, request):

        categorias = Categoria.objects.all()
        #Si se pasa un conjunto de instancias se coloca many True para que el serializardor pueda iterar y transformar cada una de las instancias
        dataSerializada = CategoriaSerializer(instance=categorias, many=True)

        #En django no se puede retornar un diccionario sino que tiene que crearse la instancia de la clase Response
        return Response(data = {
            "content": dataSerializada.data
        })

    def post(self, request:Request):
        #print(request.data) = convierte el json que mandamos por el bruno a un dict
        print(request.data)

        serializardor = CategoriaSerializer(data= request.data)
        #Si la data es valida significa que toda la info enviada es correcta y agrega toda la info al atributo validated_data
        #En caso esta mal se almacena los errores en un atributo llamado errors
        if serializardor.is_valid():
            #Solo se llama despues del serializardor.is_valid() no antes da error
            print(serializardor.validated_data) #Para saber que esta guardando
            #El serializafor al estar vinculado a un modelo internamente jala la forma de guardarlo en la base de datos con el metodo save
            serializardor.save() #Ya se guarda directamente en la BD
            return Response(data={                
                "message": "Categoria creada exitosamente",
                "contet": serializardor.data #Asi nos manda la informacion que creamos en la bd
            }, status=status.HTTP_201_CREATED)

        else:
            return Response(data={
                "message": "Error al crear la categoria",
                "content": serializardor.errors
            }, status=status.HTTP_400_BAD_REQUEST)


# GET | PUT | DELETE
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    
    #Es la forma el cual la vista se comunicara con la bd
    #Select * from categorias
    queryset = Categoria.objects.all()

    #Es la forma en la cual la vista se comunica con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer

    #lookup_field sirve para indicar el parametro que se usara para indicar la pk
    lookup_field = 'id'