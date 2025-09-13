from pydantic import BaseModel

class PagoBase(BaseModel):
    id_sesion: int
    monto: float

class PagoCreate(PagoBase):
    pass

class Pago(PagoBase):
    id: int

    class Config:
        from_attributes = True
