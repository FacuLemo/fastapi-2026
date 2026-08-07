from typing import Annotated

from pydantic import BaseModel, Field

from .tipos import BoolActivo, IntPrecioVenta, StrCortito


class ArticuloSchema(BaseModel):
    id: Annotated[int, Field(gt=0, description="ID del articulo")]
    nombre: StrCortito
    precio: IntPrecioVenta = 1500
    activo: BoolActivo = True


class ArticuloUpdateSchema(BaseModel):
    nombre: StrCortito
    precio: IntPrecioVenta = 2000
    activo: BoolActivo = True
