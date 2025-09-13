from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Fotografia(Base):
    __tablename__ = "fotografias"

    id = Column(Integer, primary_key=True, index=True)
    id_sesion = Column(Integer, ForeignKey("sesiones.id"), nullable=False)
    url = Column(String(255), nullable=False)

    sesion = relationship("Sesion", back_populates="fotografias")
