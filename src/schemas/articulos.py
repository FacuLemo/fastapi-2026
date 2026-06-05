from typing import Annotated

from pydantic import BaseModel, Field

# Modularizar los tipos personalizados (Type Aliases)
# La nomenclatura recomendada es PascalCase, entonces quedaría:
IntPositivo = Annotated[int, Field(gt=0)]
StrCortito = Annotated[str, Field(max_length=30)]
IntPrecioVenta = Annotated[int, Field(gt=500, lt=999999)]
BoolActivo = Annotated[bool, Field(description="Sigue disponible?")]


class ArticuloSchema(BaseModel):
    id: Annotated[int, Field(gt=0, description="ID del articulo", deprecated=True)]
    nombre: StrCortito
    precio: IntPrecioVenta = 1500
    activo: BoolActivo = True


class ArticuloUpdateSchema(BaseModel):
    nombre: StrCortito
    precio: IntPrecioVenta = 2000
    activo: BoolActivo = True
