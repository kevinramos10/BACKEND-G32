from flask_restful import Resource, request
from app.schemas import LibroSchema
from pydantic import ValidationError, TypeAdapter

from app.models import Libro
from app.extensions import db
from datetime import datetime

from app.util import paginationInfo
class LibrosController(Resource):

    def get(self):

        #Para saber que esta mandando el bruno
        pagina = int(request.args.get('page', 1)) 
        porPagina = int(request.args.get('perPage', 10))

        #en un controlador con pagina necesitamos saber cuantos elementos tenemos por devolver
        #Solo se necesita saber la cantidad de elemento que hay

        total = db.session.query(Libro).filter(Libro.eliminado == False).count()    

        offset = (pagina - 1) * porPagina
        limit = porPagina
        
        libros = db.session.query(Libro).filter(Libro.eliminado == False).offset(offset).limit(limit).all()
        adaptador_libro = TypeAdapter(list[LibroSchema])
        resultado = adaptador_libro.validate_python(libros)

        pageInfo = paginationInfo(total, pagina, porPagina)

        return{
            "message": "Los libros son:",
            "content": adaptador_libro.dump_python(resultado, mode='json'),
            'pageInfo': pageInfo
        }

    def post(self):

        data = request.get_json()

        try:
            informacionSerializada = LibroSchema.model_validate(data)

            # nuevoLibro = Libro(
            #     nombre = informacionSerializada.nombre,
            #     fechaPublicacion = informacionSerializada.fechaPublicacion,
            #     prologo = informacionSerializada.prologo,
            #     isbn = informacionSerializada.isbn
            # )

            nuevoLibro = Libro(**informacionSerializada.model_dump())

            db.session.add(nuevoLibro)
            db.session.commit()

            resultado = LibroSchema.model_validate(nuevoLibro).model_dump(mode='json')
            return{
                "message" : "Libro creado exitosamente",
                'content': resultado
            }, 201

        except ValidationError as error:
            return{
                "message": "Error al crear el libro",
                "content": error.errors()
            }, 400

class LibroController(Resource):
    def delete(self, id):
        libroEncontrando = db.session.query(Libro).with_entities(Libro.id).filter(Libro.id == id, Libro.eliminado == False).first()

        print(libroEncontrando)

        if not libroEncontrando:
            return{
                'message': 'Libro no existe'
            }, 404

        #Tambien se puede actualizar mediante el metodo update
        db.session.query(Libro).filter(Libro.id == id).update({
            Libro.eliminado: True
        })

        #Guardamos la inforamcion de manera permanente
        db.session.commit()


        return{
            'message':'Libro eliminado exitosamente'
        }

    def get(self, id):

        libroEncontrado = db.session.query(Libro).filter(Libro.id == id).first()

        if not libroEncontrado:
            return{
                "message": 'El libro no existe'
            }, 404

        #print(libroEncontrado.libro_categorias[0].categoria.nombre)

        categorias = []
        for libroCategoria in libroEncontrado.libro_categorias:
            categorias.append({
                "id": libroCategoria.categoria.id,
                "nombre": libroCategoria.categoria.nombre
            })


        resultado = {
            "id": libroEncontrado.id,
            "nombre": libroEncontrado.nombre,
            "fechaPublicacion": datetime.strftime(libroEncontrado.fechaPublicacion, "%Y-%m-%d/, %H:%M:%S") ,
            "prologo": libroEncontrado.prologo,
            "isbn": libroEncontrado.isbn,
            "categorias": categorias
        }   

        return{
            'content': resultado
        }


