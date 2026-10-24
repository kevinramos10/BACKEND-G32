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
                                    UpdateAPIView) #Actualizar

from rest_framework.viewsets import ViewSet

from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriasView(APIView):
    #Al usar el APIVIEW esto es muy similar al resourse de flask-restfult en el cual se puede colocar los
    #metodos http como metodos de la clase
    def get(self, request):
        #SELECT * FROM Categorias Where eliminado = False
        categorias = Categoria.objects.filter(eliminado=False).all()
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
#Si la vista generica deja de ser genera se puede convertir a un viewSet
#post = create
#get = reatrive
#get = list (si retorna varios)
#put = update
#delete = destroy
#patch = partial_update
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    
    #Es la forma el cual la vista se comunicara con la bd
    #Select * from categorias
    queryset = Categoria.objects.all()

    #Es la forma en la cual la vista se comunica con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer

    #lookup_field sirve para indicar el parametro que se usara para indicar la pk
    lookup_field = 'id'

    #Devolver solo 1 categoria
    def retrieve(self, request, id):
        # al usar el retrieve | update | destroy siempre lo enviara como 2do parametro el self no se cuenta

        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        dataSerializada = self.serializer_class(instance= categoriaEncontrada)

        return Response(data={
            "content": dataSerializada.data
        })

    def update(self, request, id):

        #Validar si existe
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = self.serializer_class(data=request.data)

        if serializador.is_valid():
            serializador.update(categoriaEncontrada, serializador.validated_data)

            return Response(data={
                "message": "Categoria actualizada existosamente",
                "content": serializador.data
            })

        else:
            return Response(data={
                "message": "Error al actualizar la categoria",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        #Validar si existe la cat
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message": "Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        # #DELETE FROM categorias Where id == '...'
        # categoriaEncontrada.delete()

        #Cambiamos el estado de eliminado a verdadero
        categoriaEncontrada.eliminado = True 
        categoriaEncontrada.save() #Guardamos

        #En un eliminado no es necesario poner un mensaje de eliminado
        #Bien se pone un mensaje o sino se poner el 204 no se pone los 2 pq esta mal
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

class ProductosView(ViewSet):
    def list(self, request):
        pass

    def create(self, request: Request):
        serializador = ProductoSerializer(data=request.data)

        if serializador.is_valid():
            serializador.save()

            return Response(data={
                "message": "Producto creado exitosamente",
                "content": serializador.data
            }, status=status.HTTP_201_CREATED)

        else:
            return Response(data={
                "message": "Error al crear la data",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)