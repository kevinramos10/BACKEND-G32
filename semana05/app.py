# from LIBRERIA import CLASES, FUNCIONES, que queremos usar de la libreria.
#request nos dara toda la informacion proveniente del cliente, y solo puede ser llamador dentro de un controlador
from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType

from os import environ #devolvera todas las variables de entorno de la maquina y aqui se agregaran las variables del archivo .env


from dotenv import load_dotenv
#El load_dotenv siempre va en la 1era linea del proyecto para que cargue las variables en todo el proyecto y evitar alguna variable no leida

load_dotenv()

from psycopg import connect

# postgresql://NOMBRE_USUARIO:PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
#credenciales = "postgresql://postgres:123456 @127.0.0.1:5432/flask_db"
credenciales = environ.get("DATABASE_URL")
conexion = connect(conninfo=credenciales)

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
        # El encargado de iniciar la conexion con la BD
        cursor = conexion.cursor()

        #Ejecuramos el comando en la bd
        cursor.execute("SELECT * FROM productos")

        # Para obtener el resultado (si es necesario) usamos los metodos fetchone, fetchall, fetchmany
        productos_bd = cursor.fetchall()
        print(productos_bd)
        cursor.close() #Cerramos la conexion de la BD, Finaliza la comunicacion

        resultado = []
        for producto in productos_bd:
            resultado.append({ 
                "id": producto[0],
                "nombre": producto[1],
                "precio": float(producto[2]),
                "cantidad": producto[3]
            })

        # Los controladores (es la logica del endpoint) suelen retornar diccionarios que estos seran interpretados en JSON o tambien se suele retornar listas (arreglos)
        return {
            "message": "Los productos son:",
            "content": resultado

        }
    elif request.method == 'POST':
        #se usa para crear nueva informacion proveniente del frontend
        # request.get_data retorna la informacion del cliente como si fuera un string
        # request.get_json retorna la infiramcion del cliente como si fuera un diccionario para que python pueda entender
        #print(request.get_data())
        #print(request.get_json())

        #handler, manejador de errores
        #Le colocamos un try ya que como no hay danos no esta trayendo nada y nos mandara error
        try:
            data = request.get_json()

            cursor = conexion.cursor() #Abrimos la conexion con la BD

            # %s hace la conversion de la inforamcion proveniente del cliente a un string sin parametros que puedan vulnerar mi BD y en los string comunes podemos utilizar %f para los flotantes y adicionalmente el %i para convertir a enteros y asi podemos evitar ataques directos a la BD a esto se le llama(SQL INYECTION)
            # Si queremos retornar la informacion que acabamos de grabar en la base de datos se puede utilizar el comando RETURNING columnas, es decir, si ponemos INSERT INTO ... VALUES ... RETURNING * esto devolvera toda la informacion agregada a la bd
            cursor.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s) RETURNING *", (
                data.get("nombre"),
                data.get("precio"),
                data.get("cantidad")))

            #Para concervar la data y asegurarnos que la nueva informacion si se guarde en la BD usamos el conexion.commit()
            conexion.commit()

            #Para obtener el nuevo producto creado y poder imprimirlo
            nuevo_producto = cursor.fetchone()
            print(nuevo_producto)

            #Cerramos la conexion
            cursor.close()

            #Ahora con la informacion correcta agregamos este producto a nuestra lista
            #productos.append(data)
            return {
                "message": "Producto creado exitosamente"
            }
        except UnsupportedMediaType:
        #except Exception as error:
            #Exceiption es la clase primordial de los errores para poder saber que error es alias es as
            #print(type(error)) #para saber el error cual es
            return {
                "message": "Se debe enviar la informacion en formato json"
            }

        



if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug=True para que al guardar el archivo ctrl + c se cargue el servidor solito y siga corriendo
    app.run(port=5000, debug=True)


