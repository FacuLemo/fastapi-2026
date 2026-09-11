# MODELO:
# Clases que representan TABLAS real en la DB
# controladas por SQLAlchemy (Base o Declarative Base)

#Ahora usamos SQLModel, que por detrás funciona con sqlalchemy.
from sqlmodel import SQLModel, Field

# VIEJO, CON SQLALCHEMY:
# class Articulo(Base): #model == tabla
#     __tablename__ = "articulos"

#     id = Column(Integer, primary_key=True)
#     nombre = Column(String)
#     stock = Column(Integer)
#     precio = Column(Integer)
#     activo = Column(Boolean)

#AHORA, con slqmodel:
class ArticuloBase(SQLModel): # parecido a ArticuloCreateUpdate
    nombre: str 
    stock:int 
    precio:int 
    activo:bool 

class Articulo(ArticuloBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class ArticuloPublic(ArticuloBase):
    id: int
