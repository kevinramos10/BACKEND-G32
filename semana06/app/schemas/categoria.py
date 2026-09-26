from pydantic import BaseModel, Field

#pydantic valida la configuracion que nosotros definamos en los atriburtos de la clase es decir utiliza la configuracion de cada atributo para que cuando le pasemos la informacion esta sea corroborada y si es valida continua sino emitira un error
class CategoriaSerializer(BaseModel):
    nombre: str = Field(examples=["Comedia","Accion"])
