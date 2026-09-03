from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, Query, Depends
from sqlalchemy.orm import Session
from database import get_db

from models.articulos import Articulo
from schemas.articulos import ArticuloSchema, ArticuloUpdateSchema

articulos_routers = APIRouter()


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


# get all articulos
@articulos_routers.get("/", response_model=list[ArticuloSchema])
async def get_articulos(db: Session = Depends(get_db)):  # Inyección de Dependencias
    articulos = db.query(Articulo).all()
    return articulos


# get by id
@articulos_routers.get(
    "/{id}",  # Parámetro de ruta (esta en la url)
    responses=NOT_FOUND_RESPONSE,
    response_model=ArticuloSchema,
)
async def get_articulos_by_id(
    id: Annotated[int, Path(gt=0)],
    db: Session = Depends(get_db)
):

    #arti_obtenido = db.query(Articulo).filter(Articulo.id == id).first()
    #SELECT * FROM articulos WHERE arti_id = 6

    arti_obtenido = db.get(Articulo, id)
    if arti_obtenido is not None:
        return arti_obtenido
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.post(
    "/", response_model=ArticuloSchema
)  # VALIDO EL DATO DE SALIDA
async def crear_articulo(articulo_nuevo: ArticuloSchema, db: Session = Depends(get_db) ):  # VALIDO EL DATO DE ENTRADA

    articulo_db = Articulo( # <- MODELO
        nombre= articulo_nuevo.nombre,
        precio = articulo_nuevo.precio,
        activo = articulo_nuevo.activo,
    )
    db.add(articulo_db)
    db.commit()
    db.refresh(articulo_db)

    #persistir en la db
    return articulo_db


# @articulos_routers.delete(
#     "/{id}",  # ?logico=false
#     responses=NOT_FOUND_RESPONSE,  # DOCUMENTACION
#     response_model=ArticuloSchema,  # VALIDACION DATOS DE SALIDA
# )
# async def borrar_articulo(
#     id: Annotated[int, Path(gt=0)],
#     logico: Annotated[bool, Query(description="Mantener registro?")] = False,
#     # ^^ los tipos de estos parámetros pueden ser modularizados, ¿no?
# ) -> ArticuloSchema:
#     for articulo in articulos:
#         if articulo["id"] == id:
#             if logico:
#                 articulo["activo"] = (False,)
#             else:
#                 articulos.remove(articulo)
#             return articulo
#     raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.put(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=ArticuloSchema
)
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    # ^^ El tipo puede ser modularizado, no?
    articulo_editar: ArticuloUpdateSchema,
    db: Session = Depends(get_db),
):

    arti_obtenido = db.get(Articulo, id)
    if arti_obtenido is not None:
        arti_obtenido.nombre = articulo_editar.nombre
        arti_obtenido.precio = articulo_editar.precio
        arti_obtenido.activo = articulo_editar.activo
        db.commit()
        db.refresh(arti_obtenido)
        return arti_obtenido
        
    raise HTTPException(status_code=404, detail="Artículo no encontrado")



@articulos_routers.patch(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=ArticuloSchema
)
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    # ^^ El tipo puede ser modularizado, no?
    articulo_editar: ArticuloUpdateSchema,
    db: Session = Depends(get_db),
):

    arti_obtenido = db.get(Articulo, id)
    if arti_obtenido is not None:
        arti_obtenido.nombre = articulo_editar.nombre
        arti_obtenido.precio = articulo_editar.precio
        arti_obtenido.activo = articulo_editar.activo
        db.commit()
        db.refresh(arti_obtenido)
        return arti_obtenido
        
    raise HTTPException(status_code=404, detail="Artículo no encontrado")
