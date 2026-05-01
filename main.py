from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

app = FastAPI()


class Articulo(BaseModel):
    id: int
    nombre: str
    precio: float
    activo: bool


class ArticuloUpdate(BaseModel):
    nombre: str
    precio: float
    activo: bool


app.title = "Mi primera API"  # Así cambia el nombre en /docs

# METODOS: 2 GET, POST PUT DELETE

# Simulación db supermercado:
articulos = [
    {"id": 1, "nombre": "Paquete de Arroz", "precio": 2000, "activo": True},
    {"id": 2, "nombre": "Fideos", "precio": 3000, "activo": True},
    {"id": 3, "nombre": "Atún Desmenuzado", "precio": 150.50, "activo": True},
]


@app.get("/articulos")
async def get_articulos() -> list[Articulo]:
    # filtrar no activos
    return articulos


@app.get("/articulos/{id}")  # Parámetro de ruta (esta en la url)
async def get_articulos_by_id(
    id: Annotated[
        int,
        Path(
            gt=0,
            description="Id a buscar entre articulos. >0",
        ),
    ],
) -> Articulo:
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    raise HTTPException(status_code=404, detail="Articulo no encontrado")


# Parámetro query-> /articulos?clave=valor&llave=valor


# validacion para int
# gt greater than : mayor que
# ge greater or equal : >= que
# lt less than : menor que
# le less or equal : <= que

# para str
# min_length
# max_length


@app.post("/articulos")  # Body
async def crear_articulo(
    articulo: Articulo,  # <- Clase BaseModel de pydantic, viene en el body
) -> Articulo:
    nuevo_articulo = (
        articulo.model_dump()
    )  # model dump convierte los datos del obj en dict
    articulos.append(nuevo_articulo)
    return nuevo_articulo


@app.delete("/articulos/{id}")  # ?logico=false
async def borrar_articulo(
    id: int, logico: bool = Query(description="Mantener registro?", default=False)
) -> Articulo:
    for articulo in articulos:
        if articulo["id"] == id:
            if logico:
                articulo["activo"] = (False,)
            else:
                articulos.remove(articulo)
            return articulo
    raise HTTPException(status_code=404, detail="Articulo no encontrado")


@app.put("/articulos/{id}")
async def editar_articulo(
    id: Annotated[int, Path(gt=0, description="Id del producto. >0")],
    articulo: ArticuloUpdate,
) -> Articulo:
    for a in articulos:
        if a["id"] == id:
            a["nombre"] = articulo.nombre
            a["precio"] = articulo.precio
            a["activo"] = articulo.activo
            return a
    raise HTTPException(status_code=404, detail="Articulo no encontrado")


"""
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
