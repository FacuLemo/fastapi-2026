from fastapi import Body, FastAPI, Path, Query

app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

# METODOS: 2 GET, POST PUT DELETE

# Simulación db supermercado:
articulos = [
    {"id": 1, "nombre": "Paquete de Arroz", "precio": 2000, "activo": True},
    {"id": 2, "nombre": "Fideos", "precio": 3000, "activo": True},
    {"id": 3, "nombre": "Atún Desmenuzado", "precio": 150.50, "activo": True},
]


@app.get("/articulos")
async def get_articulos():
    # filtrar no activos
    return articulos


@app.get("/articulos/{id}")  # Parámetro de ruta (esta en la url)
async def get_articulos_by_id(
    id: int = Path(
        gt=0,
        description="Id a buscar entre articulos. >0",
    )
):
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    return {"detail": "Not found"}


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
    id: int = Body(gt=0),
    nombre: str = Body(min_length=3, max_length=60),
    precio: float = Body(ge=1000, lt=99999999),
):
    nuevo_articulo = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
    }
    articulos.append(nuevo_articulo)
    return nuevo_articulo


@app.delete("/articulos/{id}") #?logico=false
async def borrar_articulo(
    id: int,
    logico: bool = Query(description="Mantener registro?", default=False)
):
    for articulo in articulos:
        if articulo["id"] == id:
            if logico:
                articulo["activo"]=False,
            else:
                articulos.remove(articulo)
            return {"detail": "Borrado correctamente"}
    return {"detail": "no encontrado"}


@app.put("/articulos/{id}")
async def editar_articulo(
    id: int = Path(gt=0, description="Id del producto. >0"),
    nombre: str = Body(max_length=50),
    precio: float = Body(ge=1000),
):
    for articulo in articulos:
        if articulo["id"] == id:
            articulo["nombre"] = nombre
            articulo["precio"] = precio
            return articulo

    return {"detail": "Not Found"}


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
