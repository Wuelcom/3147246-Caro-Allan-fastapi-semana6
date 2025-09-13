from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import sesion_crud
from app.schemas import sesion_schema

router = APIRouter(
    prefix="/photo/sesiones",
    tags=["Sesiones Fotográficas"]
)

@router.post("/", response_model=sesion_schema.Sesion)
def create_sesion(sesion: sesion_schema.SesionCreate, db: Session = Depends(get_db)):
    return sesion_crud.create_sesion(db, sesion)

@router.get("/{sesion_id}", response_model=sesion_schema.Sesion)
def get_sesion(sesion_id: int, db: Session = Depends(get_db)):
    db_sesion = sesion_crud.get_sesion(db, sesion_id)
    if not db_sesion:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return db_sesion

@router.get("/", response_model=list[sesion_schema.Sesion])
def get_sesiones(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return sesion_crud.get_sesiones(db, skip, limit)

@router.put("/{sesion_id}", response_model=sesion_schema.Sesion)
def update_sesion(sesion_id: int, sesion: sesion_schema.SesionUpdate, db: Session = Depends(get_db)):
    db_sesion = sesion_crud.update_sesion(db, sesion_id, sesion)
    if not db_sesion:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return db_sesion

@router.delete("/{sesion_id}")
def delete_sesion(sesion_id: int, db: Session = Depends(get_db)):
    deleted = sesion_crud.delete_sesion(db, sesion_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")
    return {"message": "Sesión eliminada"}
