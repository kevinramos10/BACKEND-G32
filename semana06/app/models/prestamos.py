from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)    
    fechaPrestamo = Column(type_=types.Date, nullable=False, name='fecha_prestamo')
    fechaDevolucion = Column(type_=types.Date, name='fecha_devolucion')

    usuarioId = Column(ForeignKey(column='usuarios.id'), name='usuario_id', nullable=False, type_=types.Integer)
    ejemplarId = Column(ForeignKey(column='ejemplares.id'), name='ejemplar_id', nullable=False, type_=types.Integer)

    usuario = relationship('Usuario', backref='prestamos')
    ejemplar = relationship('Ejemplar', backref='prestamos')

