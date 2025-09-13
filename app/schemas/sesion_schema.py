from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.models.sesion_model import EstadoSesion

class SesionBase(BaseModel):
    id_usuario: int
    fecha: date
    ubicacion: str
    tipo_sesion: str
    duracion_horas: int
    precio: float

class SesionCreate(SesionBase):
    pass

class SesionUpdate(BaseModel):
    fecha: Optional[date] = None
    ubicacion: Optional[str] = None
    tipo_sesion: Optional[str] = None
    duracion_horas: Optional[int] = None
    precio: Optional[float] = None
    estado: Optional[EstadoSesion] = None

class Sesion(SesionBase):
    id: int
    estado: EstadoSesion

    class Config:
        from_attributes = True
