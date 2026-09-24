from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class LibroCategoria(db.Model):

    __tablename__ = 'libros_categorias'

    libroId = Column(ForeignKey(column='libros.id'), nullable=False, name='libro_id', primary_key=True, type_=types.Integer)
    categoriaId = Column(ForeignKey(column='categorias.id'), nullable=False, name='categoria_id', primary_key=True, type_=types.Integer)

    #RelationShips
    #Es la relacion peroa nivel del ORM osea no afecta a la BD pero me sirve para poder acceder a los datos desde una entidad por ejemplo libros hacia sus libros_categoria
    #Creara un atributo virtual en tiempo de jecucion para poder accerde desde la instacia del libro a sus libros categorias
    #
    libro = relationship('Libro', backref='libro_categoria')
    categoria = relationship('Categoria', backref='libro_categoria')