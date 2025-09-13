from fastapi import FastAPI
from app.database import Base, engine
from app.models import usuario_model, sesion_model, fotografia_model, pago_model
from app.routers import usuario_routes, sesion_routes, fotografia_routes, pago_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Fotografía")

app.include_router(usuario_routes.router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(sesion_routes.router, prefix="/sesiones", tags=["Sesiones"])
app.include_router(fotografia_routes.router, prefix="/fotografias", tags=["Fotografías"])
app.include_router(pago_routes.router, prefix="/pagos", tags=["Pagos"])
