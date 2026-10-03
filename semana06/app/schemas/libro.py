from pydantic import BaseModel, ConfigDict, Field
from datetime import date

class LibroSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int | None = None
    nombre: str
    fechaPublicacion: date | None = None
    prologo: str | None = None
    isbn: str = Field(max_length=20)
    #Esta propiedad no debe ser utilizada por el cliente, jamas la debe observar
    #eliminado: bool = Field(default=False, exclude=True)
