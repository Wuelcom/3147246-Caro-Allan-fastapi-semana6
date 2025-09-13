from pydantic import BaseModel

class FotografiaBase(BaseModel):
    id_sesion: int
    url: str

class FotografiaCreate(FotografiaBase):
    pass

class Fotografia(FotografiaBase):
    id: int

    class Config:
        from_attributes = True
