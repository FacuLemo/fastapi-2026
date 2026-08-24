# MODELO:
# Clases que representan TABLAS real en la DB
# controladas por SQLAlchemy (Base o Declarative Base)
from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Articulo(Base):
    __tablename__ = "articulos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Integer)
    activo = Column(Boolean)


# usamos de referencia el schema:
# class ArticuloSchema(BaseModel):
    # id: Annotated[int, Field(gt=0, description="ID del articulo")]
    # nombre: StrCortito
    # precio: IntPrecioVenta = 1500
    # activo: BoolActivo = True
