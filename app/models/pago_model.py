from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    id_sesion = Column(Integer, ForeignKey("sesiones.id"), nullable=False)
    monto = Column(DECIMAL(10,2), nullable=False)

    sesion = relationship("Sesion", back_populates="pagos")
