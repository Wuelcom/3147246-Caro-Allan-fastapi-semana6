from sqlalchemy.orm import Session
from app.models.pago_model import Pago
from app.schemas.pago_schema import PagoCreate

def crear_pago(db: Session, pago: PagoCreate):
    db_pago = Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

def obtener_pago(db: Session, pago_id: int):
    return db.query(Pago).filter(Pago.id == pago_id).first()
