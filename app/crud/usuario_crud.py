from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.usuario_schema import UsuarioCreate

def crear_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(nombre=usuario.nombre, correo=usuario.correo, password=usuario.password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()
