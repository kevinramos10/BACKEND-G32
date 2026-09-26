# Todos los metodos se definiran como metodos de una clase

from flask_restful import Resource

class CategoriaController(Resource):

    def get(self):
        return{
            "message": "Las categorias son:"
        }#Su codigo por defecto es 200 sin ponerle
    

    def post(self):
        return{
            "message": "Categoria creada Exitosamente"
        }, 201 #Created