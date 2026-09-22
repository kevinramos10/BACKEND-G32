# from LIBRERIA import CLASES, FUNCIONES, que queremos usar de la libreria.
#request nos dara toda la informacion proveniente del cliente, y solo puede ser llamador dentro de un controlador
from flask import Flask, request
from werkzeug.exceptions import UnsupportedMediaType

from os import environ #devolvera todas las variables de entorno de la maquina y aqui se agregaran las variables del archivo .env

from flask_cors import CORS

from dotenv import load_dotenv
#El load_dotenv siempre va en la 1era linea del proyecto para que cargue las variables en todo el proyecto y evitar alguna variable no leida

load_dotenv()

from psycopg import connect
from psycopg.rows import dict_row

# postgresql://NOMBRE_USUARIO:PASSWORD_USUARIO@HOST:PUERTO/NOMBRE_BD
#credenciales = "postgresql://postgres:123456 @127.0.0.1:5432/flask_db"
credenciales = environ.get("DATABASE_URL")
conexion = connect(conninfo=credenciales)

# __name__ > Variable global de python que sirve para indicar si el archivo en el cual nos encontramos se esta ejecutando directamente o no en la terminal 
# python app.py > el valor de esta variable sera __main__
# python 01.py > y dentro de este archivo mando a llamar a app.py entonces el valor de __name__ sera secondary y por ende no será el archivo principal del proyecto.
# Flask se utiliza el patrón de diseño de Singleton
app = Flask(__name__)

CORS(app, origins=['http://127.0.0.1:5500'], methods=['GET', 'POST', 'PUT', 'DELETE'])

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
                #Validar si el producto[2] no esta vacio convierte a float, sino devolver el valor actual
                "precio": float(producto[2]) if producto[2] else producto[2],
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
            },201 #CREATED (Creado)
        except UnsupportedMediaType:
        #except Exception as error:
            #Exceiption es la clase primordial de los errores para poder saber que error es alias es as
            #print(type(error)) #para saber el error cual es
            return {
                "message": "Se debe enviar la informacion en formato json"
            },400 # Bad Request (Mala solicitud)

# En el endpoint cuando se coloca variable significa que esa parte recivira un valor diferente y ese valor se almacenara en la variable con ese nombre
@app.route('/producto/<id>', methods = ['GET', 'PUT', 'DELETE'])
def gestior_producto_por_id(id):

    if request.method == 'GET':

        cursor = conexion.cursor(row_factory=dict_row)

        cursor.execute("SELECT * FROM productos where id = %s", (id,))

        resultado = cursor.fetchone()

        print(resultado)

        cursor.close()
        if not resultado:
            return{
                "message":"Producto no encontrado"
            },404 #NOT Found - No encontrado

        return{
            "content": {
                "id": resultado.get("id"),
                "nombre": resultado.get("nombre"),
                "precio": float(resultado.get("precio")) if resultado.get("precio") else None,
                "cantidad": resultado.get("cantidad")
            }
        }

    elif request.method == 'PUT':
        #Cuando tenemos un error en nuestra operación y hacemos un commit, se queda pegado y no permite realizar otra operación, ya que está bloqueado. Entonces, para liberar esa operación y dejarla sin efecto, usamos el rollback para deshacer todos los cambios. Si no hay ningún error, este comando no tendrá efecto, pero tampoco lanzará un error.
        conexion.rollback()

        cursor = conexion.cursor(row_factory=dict_row) # row_factory=dict_row PARA QUE EL RESULTADO SEA DICCIONARIO Y NO TUPLA
        cursor.execute("SELECT id FROM productos WHERE id = %s", (id,))

        productos_existente = cursor.fetchone()

        if not productos_existente:
            return{
                "message": "Producto a actualizar no existe"
            },404

        #Ahora obtenemos la data proveniente del body
        data = request.get_json()

        cursor.execute("UPDATE productos SET nombre = %s, precio = %s, cantidad = %s WHERE id = %s RETURNING *" , (
            data.get("nombre"),
            data.get("precio"),
            data.get("cantidad"),
            id
        ))

        #Guardamos los cambios en la base de datos de manera permanente
        conexion.commit()

        #obtennemos la info actualizada
        productos_existente = cursor.fetchone()

        cursor.close()

        return{
            "message": "Producto actualizado exitosamente",
            "content": productos_existente
        }

    elif request.method == 'DELETE':
        conexion.rollback()
        cursor = conexion.cursor(row_factory=dict_row)

        cursor.execute("SELECT id FROM productos WHERE id  = %s", (id,))
        productos_existente = cursor.fetchone()

        if not productos_existente:
            return{
                "message": "Producto no encontrado"
            },404

        cursor.execute("DELETE FROM productos WHERE id = %s", (id, ))

        conexion.commit()

        cursor.close()

        return{
            "message": "Producto eliminado"
        }

# QUERY PARAMS
# parametros enviados por la URL en el cual el cliente pone el nombre de parametro y su valor, esto generalmente se usa para metodos GET porque en los GET JAMAS se envia BODY
@app.route('/buscar-producto')
def buscar_producto():
    print(request.args)

    return{
        "content": []
    }

# ESTO SIEMPRE VA AL FINAL!!!!
if __name__ == "__main__":
    # el metodo run ejecuta el servidor y lo mantiene escuchando peticiones
    # debug=True para que al guardar el archivo ctrl + c se cargue el servidor solito y siga corriendo
    app.run(port=5000, debug=True)


