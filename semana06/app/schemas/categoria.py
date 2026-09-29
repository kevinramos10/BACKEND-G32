from pydantic import BaseModel, Field, ConfigDict


#pydantic valida la configuracion que nosotros definamos en los atriburtos de la clase es decir utiliza la configuracion de cada atributo para que cuando le pasemos la informacion esta sea corroborada y si es valida continua sino emitira un error
class CategoriaSerializer(BaseModel):
    #Serializador Valida la data si es correcta la data que llega a este
    nombre: str = Field(examples=["Comedia","Accion"])

class CategoriaDeserializer(BaseModel):
    #Deserializador: Transforma la data proveniente de mi entorno python y devolvera un formato legible
    #model_config es un atributo popio de l aclase BaseModel que sirve para mofivicar todo el modelo en su totalidad y no solamente un solo atributo

    model_config = ConfigDict(from_attributes=True)

    #A los deesrializadores no es necesario agregarle resctricciones ya que solo se usara para convertir la data de instancias de clase a diccionarios

    id: int 
    nombre: str

class CategoriaSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    #Para cuando se intente crear una nueva categoria el id no debe enviarse
    #Al poner None esto indica que puede ser opcional no obligatorio
    id: int | None = Field(default=None)
    nombre: str = Field(min_length=1, examples=["Ciencia Ficcion", "Comedia"])