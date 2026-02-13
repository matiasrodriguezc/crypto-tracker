from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Buscamos la URL de la DB en las variables de entorno, o usamos una por defecto para local
# Formato: postgresql://usuario:password@servidor:puerto/nombre_db
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://user:password@postgres:5432/crypto_db"
)

# Creamos el motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creamos la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# La clase base para nuestros modelos
Base = declarative_base()