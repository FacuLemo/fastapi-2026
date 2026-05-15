from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

# Request -> Middleware -> Path Operation -> Middleware -> Response

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # entorno desarrollo
        "https://faculemo.github.io/front",  # entorno producción
        # "*", wildcard ! Cualquier origen
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# METODOS: 2 GET, POST PUT DELETE
# DRY : DON'T REPEAT YOURSELF

not_found = {
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


STR_CORTITO = Annotated[str, Field(max_length=30)]
PRECIO_PVP = Annotated[float, Field(lt=999999)]
BOOL_ACTIVO = Annotated[bool, Field(description="Disponible?")]


class ArticuloSchema(BaseModel):
    id: Annotated[int, Field(gt=0, description="ID del articulo", deprecated=True)]
    nombre: STR_CORTITO
    precio: PRECIO_PVP = 1500
    activo: BOOL_ACTIVO = True


class ArticuloUpdateSchema(BaseModel):
    nombre: STR_CORTITO
    precio: PRECIO_PVP = 2000
    activo: BOOL_ACTIVO = True


# Simulación db supermercado:
articulos = [
    {"id": 1, "nombre": "Paquete de Arroz", "precio": 2000, "activo": True},
    {"id": 2, "nombre": "Fideos", "precio": 3000, "activo": True},
    {"id": 3, "nombre": "Atún Desmenuzado", "precio": 150.50, "activo": True},
]


@app.get("/articulos", response_model=list[ArticuloSchema])
async def get_articulos():
    return articulos


@app.get(
    "/articulos/{id}",  # Parámetro de ruta (esta en la url)
    responses=not_found,
    response_model=ArticuloSchema,
)
async def get_articulos_by_id(
    id: Annotated[int, Path(gt=0)],
):
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@app.post("/articulos", response_model=list[ArticuloSchema])
async def crear_articulo(articulo_nuevo: ArticuloSchema):
    articulos.append(articulo_nuevo.model_dump())
    return articulos


@app.delete(
    "/articulos/{id}",  # ?logico=false
    responses=not_found,
    response_model=ArticuloSchema,
)
async def borrar_articulo(
    id: Annotated[int, Path(gt=0)],
    logico: Annotated[bool, Query(description="Mantener registro?")] = False,
) -> ArticuloSchema:
    for articulo in articulos:
        if articulo["id"] == id:
            if logico:
                articulo["activo"] = (False,)
            else:
                articulos.remove(articulo)
            return articulo
    raise HTTPException(status_code=404, detail="Artículo no encontrado")


@app.put("/articulos/{id}", responses=not_found, response_model=ArticuloSchema)
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    articulo_editar: ArticuloUpdateSchema,
):
    for articulo in articulos:
        if articulo["id"] == id:
            articulo["nombre"] = articulo_editar.nombre
            articulo["precio"] = articulo_editar.precio
            articulo["activo"] = articulo_editar.activo
            return articulo
    raise HTTPException(status_code=404, detail="Articulo no encontrado")


"""

# Parámetro query-> /articulos?clave=valor&llave=valor


# validacion para int
# gt greater than : mayor que
# ge greater or equal : >= que
# lt less than : menor que
# le less or equal : <= que
# max_digits / min_digits

# para str
# min_length
# max_length


@app.get("/saludo")  # "/Saludo" es el endpoint de la url
async def saludo():
    return {"hola": "mundo"}


@app.put("/saludo/put")
async def put():
    return {"hola": "put"}


@app.post("/saludo/post")
async def post():
    return {"hola": "post"}


@app.delete("/saludo/delete")
async def delete():
    return {"hola": "delete"}
"""
