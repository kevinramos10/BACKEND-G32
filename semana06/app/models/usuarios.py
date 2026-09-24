from app.extensions import db
from sqlalchemy import Column, types

class Usuario(db.Model):

    __tablename__ ="usuarios"

    #Completar comentarios
    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text)

    apellidoPaterno = db.Column(name='apellido_pat', type_=types.Text, nullable=False)

    apellidoMaterno = Column(name='apellido_mat', type_=types.Text)

    correo = Column(type_=types.Text, unique=True, nullable=False)
    fechaBacimiento = Column(name='fecha_nacimiento', type_=types.Date)


