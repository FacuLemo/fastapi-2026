# MODELO:
# Clases que representan TABLAS real en la DB
# controladas por SQLAlchemy (Base o Declarative Base)

# Ahora usamos SQLModel, que por detrás funciona con sqlalchemy.
from sqlmodel import Field, SQLModel

# VIEJO, CON SQLALCHEMY:
# class Articulo(Base): #model == tabla
#     __tablename__ = "articulos"

#     id = Column(Integer, primary_key=True)
#     nombre = Column(String)
#     stock = Column(Integer)
#     precio = Column(Integer)
#     activo = Column(Boolean)


# AHORA, con slqmodel:
class ArticuloBase(SQLModel):  # parecido a ArticuloCreateUpdate
    nombre: str = Field(max_length=90)
    stock: int | None
    proveedor: str | None
    precio: int
    activo: bool


class Articulo(ArticuloBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ArticuloPublic(ArticuloBase):
    id: int


# class Proveedor(SQLModel, table=True):
#    id: int | None = Field(default=None, primary_key=True)
#     nombre: str
