from sqlmodel import Field, Relationship, SQLModel


# Consultar articulos.py para explicación más detallada
class ProveedorBase(SQLModel):
    nombre: str = Field(max_length=90)
    telefono: str


class Proveedor(ProveedorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # Para evitar import circular, Articulo va en str
    articulos: list["Articulo"] | None = Relationship(back_populates="proveedor")


class ProveedorPublic(ProveedorBase):
    id: int
