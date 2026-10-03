# Todos los metodos se definiran como metodos de una clase

from flask_restful import Resource, request
from app.schemas import CategoriaSchema
from pydantic import ValidationError, TypeAdapter

from app.models import Categoria
from app.extensions import db

class CategoriasController(Resource):

    def get(self):

        #SELECT * FROM categorias;
        categorias = db.session.query(Categoria).all()
        print(categorias)

        adaptador_categoria = TypeAdapter(list[CategoriaSchema])

        resultado = adaptador_categoria.validate_python(categorias)
        print(resultado)

        return{
            "message": "Las categorias son:",
            "content": adaptador_categoria.dump_python(resultado, mode='json')
        }#Su codigo por defecto es 200 sin ponerle
    

    def post(self):
        data = request.get_json()

        # Al momento de validar la info falla este emite un erro de tipo validationerrro
        try:
            print(CategoriaSchema.model_json_schema())
            informacionSerializada = CategoriaSchema.model_validate(data)
            print(informacionSerializada)

            #Ahora que sabemos que la informacion es correcta guardaremos en la Bd
            #Esto es igual que la query en la BD= insert into cateogiras(..) VALUES (...)
            nuevaCategoria = Categoria(nombre = informacionSerializada.nombre)
            #Aca agregamos el nuevo registro a la bd
            db.session.add(nuevaCategoria)
            #Guardar el registro de manera permanente
            db.session.commit()

            return{
                "message": "Categoria creada Exitosamente"
            }, 201 #Created
        except ValidationError as error:
            return{
                "message" : "Error al crear la categoria",
                "content" : error.errors()
            }, 405 #Bad Request


class CategoriaController(Resource):
    #Esta sera la encargada de la gestion de 1 sola categoria segun su id

    def validarCategoria(self, id):
         # el filter se usa en comparacion > filter(Categoria.id == 1)
        # el filter_by se usa en asigancion > filtaer_by(id=1)
        #SELECT * FROM CATEGORIAS WHERE ID = .... LIMIT 1
        categoriaEncontrada = db.session.query(Categoria).filter(Categoria.id == id).first()
        return categoriaEncontrada
        


    def get(self, id):

        categoriaEncontrada = self.validarCategoria(id)

        if not (categoriaEncontrada):
            return {
                'message': 'Categoria no existe'
            }, 404

        respuesta = CategoriaSchema.model_validate(categoriaEncontrada).model_dump()

        print(categoriaEncontrada.libro_categorias)

        cantidad = len(categoriaEncontrada.libro_categorias)

        #Es igual
        # cant = 0
        # for libroCategoria in categoriaEncontrada.libro_categorias:
        #     cant = cant + 1

        respuesta["libros"] = cantidad

        return{
            'content': respuesta
        }


    def put(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        
        if not (categoriaEncontrada):
            return {
                'message': 'Categoria no existe'
            }, 404

        categoriaValidada = CategoriaSchema.model_validate(request.get_json())

        categoriaEncontrada.nombre = categoriaValidada.nombre

        db.session.commit()

        resultado = CategoriaSchema.model_validate(categoriaEncontrada).model_dump()

        return{
            'message': 'Categoria modificada exitosamente',
            'content': resultado
        }

    def delete(self, id):
        categoriaEncontrada = self.validarCategoria(id)
                
        if not (categoriaEncontrada):
            return {
                'message': 'Categoria no existe'
            }, 404

        db.session.query(Categoria).filter(Categoria.id == id).delete()

        db.session.commit()

        # En los delete permanentes se suele no retornar nada y solo retornar un estado 204
        #204 sin contenido
        return None, 204

