# Todos los metodos se definiran como metodos de una clase

from flask_restful import Resource, request
from app.schemas import CategoriaSerializer
from pydantic import ValidationError

from app.models import Categoria
from app.extensions import db

class CategoriaController(Resource):

    def get(self):
        

        return{
            "message": "Las categorias son:"
        }#Su codigo por defecto es 200 sin ponerle
    

    def post(self):
        data = request.get_json()

        # Al momento de validar la info falla este emite un erro de tipo validationerrro
        try:
            informacionSerializada = CategoriaSerializer.model_validate(data)
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