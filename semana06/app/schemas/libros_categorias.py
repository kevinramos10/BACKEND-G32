from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator, TypeAdapter
from typing import Annotated

ListaIds = Annotated[list[PositiveInt], Field(min_length=1, max_length=100)]

class LibrosCategoriasSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    libroId: int = Field(min=1)
    categoriaIds: ListaIds = Field()

    @field_validator('categoriaIds')
    def eliminar_duplicados(cls, valor):

        #return list(dict.fromkeys(valor))
        return list(set(valor))

