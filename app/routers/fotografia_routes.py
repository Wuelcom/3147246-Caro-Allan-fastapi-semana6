from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import fotografia_crud
from app.schemas import fotografia_schema

router = APIRouter()

@router.post("/", response_model=fotografia_schema.Fotografia)
def crear_fotografia(foto: fotografia_schema.FotografiaCreate, db: Session = Depends(get_db)):
    return fotografia_crud.crear_fotografia(db, foto)

@router.get("/{foto_id}", response_model=fotografia_schema.Fotografia)
def obtener_fotografia(foto_id: int, db: Session = Depends(get_db)):
    db_foto = fotografia_crud.obtener_fotografia(db, foto_id)
    if not db_foto:
        raise HTTPException(status_code=404, detail="Fotografía no encontrada")
    return db_foto
