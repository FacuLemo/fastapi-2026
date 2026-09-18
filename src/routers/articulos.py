from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query

# Ahora que usamos sqlmodel no traemos nada de sqlalchemy.
from sqlmodel import Session, select

from database import get_db

# Y también nuestros schemas son los models. (fíjense los response_model)
from models.articulos import Articulo, ArticuloBase, ArticuloPublic

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
@articulos_routers.get("/", response_model=list[ArticuloPublic])
async def get_articulos(db: Session = Depends(get_db)):  # Inyección de Dependencias
    # EN SQL SERÍA: SELECT * FROM articulos
    # CON SQLALCHEMY: articulos = db.query(Articulo).all() en sqlalchemy
    articulos = db.exec(select(Articulo)).all()  # en sqlmodel
    return articulos


# get by id
@articulos_routers.get(
    "/{id}",  # Parámetro de ruta (esta en la url)
    responses=NOT_FOUND_RESPONSE,
    response_model=ArticuloPublic,
)
async def get_articulos_by_id(
    id: Annotated[int, Path(gt=0)], db: Session = Depends(get_db)
):

    # arti_obtenido = db.query(Articulo).filter(Articulo.id == id).first()
    # SELECT * FROM articulos WHERE arti_id = 6

    arti_obtenido = db.get(Articulo, id)
    if arti_obtenido is not None:
        return arti_obtenido
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.post("/", response_model=ArticuloPublic)  # VALIDO EL DATO DE SALIDA
async def crear_articulo(
    articulo_nuevo: ArticuloBase, db: Session = Depends(get_db)
):  # VALIDO EL DATO DE ENTRADA

    # Ya no instancio ningún Objeto, sino que hago model_validate
    articulo_db = Articulo.model_validate(articulo_nuevo)
    db.add(articulo_db)
    # persistimos en la db con commit
    db.commit()
    # refrescamos UNA INSTANCIA (objeto)
    db.refresh(articulo_db)
    return articulo_db


@articulos_routers.put(
    "/{id}", responses=NOT_FOUND_RESPONSE, response_model=ArticuloPublic
)
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    # ^^ El tipo puede ser modularizado, no?
    articulo_editar: ArticuloBase,
    db: Session = Depends(get_db),
):

    arti_obtenido = db.get(Articulo, id)

    if arti_obtenido is not None:
        arti_obtenido.nombre = articulo_editar.nombre
        arti_obtenido.precio = articulo_editar.precio
        arti_obtenido.activo = articulo_editar.activo
        arti_obtenido.proveedor = articulo_editar.proveedor
        db.commit()
        db.refresh(arti_obtenido)
        return arti_obtenido

    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@articulos_routers.delete(
    "/{id}",  # ?logico=false
    responses=NOT_FOUND_RESPONSE,  # DOCUMENTACION
    response_model=list[ArticuloPublic],  # VALIDACION DATOS DE SALIDA
)
async def borrar_articulo(
    id: Annotated[int, Path(gt=0)],
    db: Annotated[Session, Depends(get_db)],
    logico: Annotated[bool, Query(description="Mantener registro?")] = False,
) -> ArticuloPublic:

    arti_obtenido = db.get(Articulo, id)
    if arti_obtenido is not None:
        if logico:
            arti_obtenido.activo = False
        else:
            db.delete(arti_obtenido)
            db.commit()
        return db.exec(select(Articulo)).all()
    raise HTTPException(status_code=404, detail="Artículo no encontrado")
