from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum

class EstadoEjemplar(Enum):    
    DISPONIBLE = 'DISPONIBLE'
    PRESTADO = 'PRESTADO'
    NO_DISPONIBLE = 'NO_DISPONIBLE'

class Ejemplar(db.Model):
    __tablename__ = 'ejemplares'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    libroId = Column(ForeignKey(column='libros.id'), name='libro_id', nullable=False, type_=types.Integer)
    codigoInventario = Column(type_=types.VARCHAR(100), nullable=False, name='codigo_inventario')
    estado = Column(type_=types.Enum(EstadoEjemplar), default=EstadoEjemplar.DISPONIBLE)

    libro = relationship('Libro', backref='libro_ejemplares')

