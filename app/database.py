from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Archivo SQLite en tu proyecto
SQLALCHEMY_DATABASE_URL = "sqlite:///./fotografia.db"

# engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal para cada request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para tus modelos
Base = declarative_base()

# Dependency para obtener la sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
