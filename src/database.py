
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#Database.py
#Gestión de la conexión a la DB -> Usando SQLAlchemy

url = "sqlite:///./base_de_datos.db" #Sqlite: DB LOCAL (no en un servidor/nube)

#Fastapi es asíncrono, entonces le hace falta args especiales (check_same_thread)
#Motor de conexión -> Prepara internamente la DB
engine = create_engine(url, connect_args={"check_same_thread":False})

#Nos permite la conexión a través del motor -> Permite el ida y vuelta
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base -> MODELOS -> Clase que representa TABLA
Base = declarative_base()

#Dependencia a inyectar en los Path Operations
def get_db():
    db = SessionLocal()
    try:
        yield db # Return que no termina la función
    finally:
        db.close()

