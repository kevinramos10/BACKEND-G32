from app.extensions import db
from sqlalchemy import Column, types
from enum import Enum

#Tenemos que crear un enumerador para el estado limitar a posibles valores solo podria hacer 2 valores no otros distintios
class EstadoEscritor(Enum):
    #Al heredar del la clase enum...
    VIVO = 'VIVO'
    MUERTO = 'MUERTO'


class Escritor(db.Model):

    __tablename__ = 'escritores'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellidos = Column(type_=types.Text, nullable=False)
    nacionalidad = Column(type_=types.Text)

    #Para crear valores por defecto se usa el valor definido en DEFAULT
    estado = Column(type_=types.Enum(EstadoEscritor), nullable=False, default=EstadoEscritor.VIVO)
