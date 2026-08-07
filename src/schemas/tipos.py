from typing import Annotated

from pydantic import Field

# Modularizar los tipos personalizados (Type Aliases)
# La nomenclatura recomendada es PascalCase, entonces quedaría:

IntPositivo = Annotated[int, Field(gt=0)]
StrCortito = Annotated[str, Field(max_length=30)]
IntPrecioVenta = Annotated[int, Field(gt=500, lt=999999)]
BoolActivo = Annotated[bool, Field(description="Sigue disponible?")]
