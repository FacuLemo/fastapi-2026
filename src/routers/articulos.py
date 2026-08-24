from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, Query

from schemas.articulos import ArticuloSchema, ArticuloUpdateSchema

articulos_routers = APIRouter()


articulos = [
    {"id": 1, "nombre": "Paquete de Arroz", "precio": 2000, "activo": True},
    {"id": 2, "nombre": "Fideos", "precio": 3000, "activo": True},
    {"id": 3, "nombre": "Atún Desmenuzado", "precio": 550, "activo": True},
]
# Constante, mayúsculas con snake_case
NOT_FOUND_RESPONSE = {
    404: {
        "description": "Response not found si no se encuentra el id",
        "content": {
            "application/json": {
                "example": {
                    "detail": "Artículo no encontrado",
                }
            }
        },
    },
}

#get all articulos
@articulos_routers.get("/", response_model=list[ArticuloSchema])
async def get_articulos():
    # Aquí mostrar únicamente articulos que activo=True
    # ^^relevante si el borrado del delete es lógico
    
    # pronto: articulos = db.query(Articulos).all()
    return articulos

#get by id
@articulos_routers.get(
    "/{id}",  # Parámetro de ruta (esta en la url)
    responses=NOT_FOUND_RESPONSE,
    response_model=ArticuloSchema,
)
async def get_articulos_by_id(
    id: Annotated[int, Path(gt=0)],
):
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.post("/", response_model=list[ArticuloSchema]) #VALIDO EL DATO DE SALIDA
async def crear_articulo(articulo_nuevo: ArticuloSchema): #VALIDO EL DATO DE ENTRADA
    articulos.append(articulo_nuevo.model_dump())
    return articulos


@articulos_routers.delete(
    "/{id}",  # ?logico=false
    responses=NOT_FOUND_RESPONSE, #DOCUMENTACION
    response_model=ArticuloSchema, #VALIDACION DATOS DE SALIDA
)
async def borrar_articulo(
    id: Annotated[int, Path(gt=0)],
    logico: Annotated[bool, Query(description="Mantener registro?")] = False,
    # ^^ los tipos de estos parámetros pueden ser modularizados, ¿no?
) -> ArticuloSchema:
    for articulo in articulos:
        if articulo["id"] == id:
            if logico:
                articulo["activo"] = (False,)
            else:
                articulos.remove(articulo)
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.put(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=ArticuloSchema
)
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    # ^^ El tipo puede ser modularizado, no?
    articulo_editar: ArticuloUpdateSchema,
):
    for articulo in articulos:
        if articulo["id"] == id:
            articulo["nombre"] = articulo_editar.nombre
            articulo["precio"] = articulo_editar.precio
            articulo["activo"] = articulo_editar.activo
            return articulo
    raise HTTPException(status_code=404, detail="Articulo no encontrado")
