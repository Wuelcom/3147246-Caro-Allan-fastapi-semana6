from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import usuario_crud
from app.schemas import usuario_schema

router = APIRouter()

@router.post("/", response_model=usuario_schema.Usuario)
def crear_usuario(usuario: usuario_schema.UsuarioCreate, db: Session = Depends(get_db)):
    return usuario_crud.crear_usuario(db, usuario)

@router.get("/{usuario_id}", response_model=usuario_schema.Usuario)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = usuario_crud.obtener_usuario(db, usuario_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
