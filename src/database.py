
#NO USAMOS MÁS SQLALCHEMY. Ahora todo sqlmodel:
from sqlmodel import create_engine, Session, SQLModel

#Database.py
#Gestión de la conexión a la DB -> Usando SQLAlchemy
url = "sqlite:///./base_de_datos.db" #Sqlite: DB LOCAL (no en un servidor/nube)

#Fastapi es asíncrono, entonces le hace falta args especiales (check_same_thread)
#Motor de conexión -> Prepara internamente la DB
engine = create_engine(url, connect_args={"check_same_thread":False})

#YA NO SE USA SESSIONMAKER (ver historial de commits para ver cómo era)

#Dependencia a inyectar en los Path Operations (Adaptada sqlmodel)
def get_db():
    with Session(engine) as session:
        yield session

