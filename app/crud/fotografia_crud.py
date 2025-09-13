from sqlalchemy.orm import Session
from app.models.fotografia_model import Fotografia
from app.schemas.fotografia_schema import FotografiaCreate

def crear_fotografia(db: Session, fotografia: FotografiaCreate):
    db_foto = Fotografia(**fotografia.dict())
    db.add(db_foto)
    db.commit()
    db.refresh(db_foto)
    return db_foto

def obtener_fotografia(db: Session, fotografia_id: int):
    return db.query(Fotografia).filter(Fotografia.id == fotografia_id).first()
