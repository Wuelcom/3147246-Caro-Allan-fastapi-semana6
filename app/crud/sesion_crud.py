from sqlalchemy.orm import Session
from app.models.sesion_model import Sesion
from app.schemas.sesion_schema import SesionCreate, SesionUpdate

def create_sesion(db: Session, sesion: SesionCreate):
    db_sesion = Sesion(**sesion.dict())
    db.add(db_sesion)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion

def get_sesion(db: Session, sesion_id: int):
    return db.query(Sesion).filter(Sesion.id == sesion_id).first()

def get_sesiones(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Sesion).offset(skip).limit(limit).all()

def update_sesion(db: Session, sesion_id: int, sesion_update: SesionUpdate):
    db_sesion = get_sesion(db, sesion_id)
    if not db_sesion:
        return None
    for field, value in sesion_update.dict(exclude_unset=True).items():
        setattr(db_sesion, field, value)
    db.commit()
    db.refresh(db_sesion)
    return db_sesion

def delete_sesion(db: Session, sesion_id: int):
    db_sesion = get_sesion(db, sesion_id)
    if not db_sesion:
        return False
    db.delete(db_sesion)
    db.commit()
    return True
