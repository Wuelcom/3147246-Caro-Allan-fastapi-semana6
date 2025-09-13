from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import pago_crud
from app.schemas import pago_schema

router = APIRouter()

@router.post("/", response_model=pago_schema.Pago)
def crear_pago(pago: pago_schema.PagoCreate, db: Session = Depends(get_db)):
    return pago_crud.crear_pago(db, pago)

@router.get("/{pago_id}", response_model=pago_schema.Pago)
def obtener_pago(pago_id: int, db: Session = Depends(get_db)):
    db_pago = pago_crud.obtener_pago(db, pago_id)
    if not db_pago:
        raise HTTPException(status_code=404, detail="Pago no encontrado")
    return db_pago
