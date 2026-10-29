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
from rest_framework.decorators import api_view

from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, ProductoDetalleSerializer, GenerarUrlAWSSerializer
from uuid import UUID

#Para conectar con el aws generar 
from boto3 import client
from os import getenv
from urllib.parse import unquote


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
    def list(self, request: Request):
        #Al usar el get en un query.paramt solo retorna la 1era informacion del query parants solo toma el 1ero
        #En cambio el getList obtiene todos los valores y los retorna en formato de lista para poder ser iterados

        categoria = request.query_params.getlist('categoria')
        nombre = request.query_params.get('nombre')

        filtros = {
            "eliminado": False
        }
            
        if categoria:
            filtros["categoria__in"] = [] #Para que sepa que estamos pasando una lista de categorias le ponemos el __in
            for categoriaId in categoria:
                #Validamos si el id de la categoria es un uuid valido, para evitar un error del lado de la bd
                try:
                    UUID(categoriaId)
                except:
                    return Response(data={
                        "message": f"El id de la categoria {categoriaId} es invalido"
                    })
                categoriaEncontrada = Categoria.objects.filter(id = categoriaId, eliminado = False).first()
                
                if categoriaEncontrada:
                    filtros["categoria__in"].append(str(categoriaEncontrada.id))        

            #Validamos que si al final todas las categorias enviadas no existen no agregamos ese filtro a la variable
            if len(filtros["categoria__in"]) == 0:
                del filtros["categoria__in"] #eliminamos la clave categoria del diccionario

        if nombre:
            # icontains funciona igual que el ILIKE para que no importe las mayusculas e minisculas
            filtros["nombre__icontains"] = nombre
        print(filtros)
        #al usar ** estamos indicando que las llaves se convertiran a parametros y sus valores se convertiran a valores de los parametros
        #ejemplo:
        #data={"nombre":"eduardo"} - **data - (nombre="eduardo") lo convierte
        productos = Producto.objects.filter(**filtros).all()
        serializador = ProductoSerializer(instance = productos, many=True)
        return Response(data={
            "content": serializador.data
        })


    def create(self, request: Request):
        serializador = ProductoSerializer(data=request.data)

        #Validar si la categoria enviada no ha sido eliminada, si esta eliminada entonces no proceder con la creacion del producto
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = request.data.get("categoria")).first()

        if not categoriaEncontrada:
            return Response(data={
                "message": "Error al crear el producto",
                "content": "Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

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



class ProductoView(ViewSet):

    def retrieve(self, request:Request, id):

        productoEncontrado = Producto.objects.filter(id = id, eliminado = False).first()

        if not productoEncontrado:
            return Response(data={
                "message": "Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoDetalleSerializer(instance = productoEncontrado)

        return Response(data={
            "content": serializador.data
        })

    def destroy(self, request:Request, id):
        productoEncontrado = Producto.objects.filter(id = id, eliminado = False).first()
        
        if not productoEncontrado:
            return Response(data={
                "message": "Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        #Hacemos el eliminado cambiando el estado a True y luego guardandolo en la bd
        productoEncontrado.eliminado = True
        productoEncontrado.save()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST'])
def crearUrlParaSubirArchivo(request:Request):
    serializador = GenerarUrlAWSSerializer(data=request.data)
    if serializador.is_valid():
        fileName = serializador.validated_data.get("fileName")
        ext = serializador.validated_data.get("ext")
        contentType = serializador.validated_data.get("contentType")
        folder = serializador.validated_data.get("folder", "/")

        s3 = client('s3')
        url = s3.generate_presigned_url(
            ClientMethod = 'put_object',
            Params={
                "Bucket":getenv('BUCKET_NAME'),
                "Key": folder + fileName + ext,
                "ContentType": contentType
            },
            ExpiresIn=150
        )
        return Response(data={
            "content": unquote(url)
        })
    else:
        return Response(data={
            "message": "Error al generar la URL",
            "content": serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)

