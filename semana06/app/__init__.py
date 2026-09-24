from flask import Flask
from .config import config_map
from .models import *
from .extensions import db, migrate



#Al usar el patron de dise;o application factory se recomienda crear una funcion llamda create_app en la cual se inicializara todo el proyecto y asi mismo puede recibir parametros para los diferentes entornos de prueba
def create_app(env = "development"):
    app = Flask(__name__)

    #from_object = Actializa los valores que le pasemos en el parametro para que la instancia de flask arranque con esas moficaciones de sus parametros por ejemplo: Debug, entre otros
    app.config.from_object(config_map[env])

    #inicilizamos la instancia de la bd pasandole la instacia de flask para que utilice las variavles que gemos configurado e la instacia (config_map)
    db.init_app(app)

    #Inicializamos la instacia de las migraciones para ahora declara nuestra configuracion de la instacia de flask y nuestra configracion de la base de datos 
    migrate.init_app(app, db)

    return app