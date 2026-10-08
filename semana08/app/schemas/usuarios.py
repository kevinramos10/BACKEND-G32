from pydantic import BaseModel, Field, EmailStr, field_validator
from re import search

class RegistroUsuarioSchema(BaseModel):

    correo: EmailStr = Field(max_length=100)
    password: str = Field(min_length=8, max_length=128)
    nombre: str = Field(min_length=1)
    apellido: str | None = Field(default=None)

    @field_validator("correo")
    def normalizar_correo(cls, valor):
        return valor.lower()

    @field_validator("password")
    def validar_password(cls, valor):
        errores = []

        if not search(r"[A-Z]", valor):
            errores.append("Falta una mayuscula")

        if not search(r"[a-z]", valor):
            errores.append("Falta una minuscula")

        if not search(r"\d", valor):
            errores.append("Falta un numero")

        if not search(r"[^A-Za-z0-9]", valor):
            errores.append("Falta un caracter especial")

        if errores:
            raise ValueError("La contrase;a requiere".join(errores))

        return valor


class LoginUsuarioSchema(BaseModel):
    correo: EmailStr
    password: str