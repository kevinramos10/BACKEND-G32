from os import getenv

#El archivo config servira para setear (asignar) las variables que se usaran en flask ya bien sea en develoment o production
class Base:
    # esta propiedad sirve para poder indicar si queremos que SQLALCHEMY nos muestre el seguimiento de las moficiaciones en la base de datos
    SQLALCHEMY_TRACK_MODIFICARIONS = False

class Development(Base):
    DEBUG = True #Esta propiedad permitira que se actualice automaticamente el servidor al guardar cualquier cambio
    #Esta variable sirve para contener la cadena de conexion a nuestra BD
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")


class Production(Base):
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")

# Diccionario con el mapeo con todas las opciones de configuracion se puede tener mas en el caso que tegamos Staging, PreProduction, Debugging, etc
config_map = {
    "development": Development,
    "production": Production
}