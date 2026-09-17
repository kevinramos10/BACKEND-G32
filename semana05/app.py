# from LIBRERIA import CLASES, FUNCIONES, que queremos usar de la libreria.
#request nos dara toda la informacion proveniente del cliente, y solo puede ser llamador dentro de un controlador
from flask import Flask, request

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se esta ejecutando directamente o no en la terminal 
# python app.py > el valor de esta variable sera __main__
# python 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ sera secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patrón de diseño de Singleton
app = Flask(__name__)

productos = [
    {
        "id": 1, 
        "nombre":"Vaso de vidrio"
    }, 
    {
        "id":2, 
        "nombre":"Parlante"
    },
    {
        "id":3,
        "nombre":"Botella de agua"
    }]

# Cada ruta (endpoint) punto final (punto de acceso)
@app.route('/estado') #despues de un decorador viene una funcion siempre
def estado_servidor():
    #es de suma importancia que en los endpoint siempre se retorne algo
    return 'El servidor esta vivo!'

#Si no se declara el parametro methods, el valor por defecto sera GET unicamente
@app.route('/productos', methods = ['GET', 'POST'])
def gestionar_productos():
    print(request.method)

    if request.method == 'GET':
        # Los controladores (es la logica del endpoint) suelen retornar diccionarios que estos seran interpretados en JSON o tambien se suele retornar listas (arreglos)
        return {
            "message": "Los productos son:",
            "content": productos
        }
    elif request.method == 'POST':
        return {
            "message": "Producto creado exitosamente"
        }



if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug=True para que al guardar el archivo ctrl + c se cargue el servidor solito y siga corriendo
    app.run(port=5000, debug=True)


