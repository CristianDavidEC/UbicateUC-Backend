from pydantic import BaseModel, Field
from bson import ObjectId


class Sitio(BaseModel):
    _id: ObjectId
    nombre: str = Field(...)
    descripcion: str = Field(...)
    latitud: str = Field(...)
    longitud: str = Field(...)
    tipo: str = Field(...)
    sede: str = Field(...)
    estado: str = Field(...)
    bloque: str = Field(...)
    piso: str = Field(...)

