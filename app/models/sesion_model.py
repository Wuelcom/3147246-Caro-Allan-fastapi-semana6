from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class EstadoSesion(str, enum.Enum):
    Pendiente = "Pendiente"
    Confirmada = "Confirmada"
    Completada = "Completada"
    Cancelada = "Cancelada"

class Sesion(Base):
    __tablename__ = "sesiones"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha = Column(Date, nullable=False)
    ubicacion = Column(String(150), nullable=False)
    tipo_sesion = Column(String(50), nullable=False)
    duracion_horas = Column(Integer, nullable=False)
    precio = Column(DECIMAL(10,2), nullable=False)
    estado = Column(Enum(EstadoSesion), default=EstadoSesion.Pendiente)

    usuario = relationship("Usuario", back_populates="sesiones")
    fotografias = relationship("Fotografia", back_populates="sesion")
    pagos = relationship("Pago", back_populates="sesion")
