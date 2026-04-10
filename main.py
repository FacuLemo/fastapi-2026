from fastapi import FastAPI

app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

# METODOS: GET POST PUT DELETE

# Simulación db supermercado:
articulos = [
    {"id": 1, "nombre": "Paquete de Arroz", "precio": 2000},
    {"id": 2, "nombre": "Fideos", "precio": 3000},
    {"id": 3, "nombre": "Atún Desmenuzado", "precio": 150.50},
]


@app.get("/articulos")
async def get_articulos():
    return articulos


@app.get("/articulos/{id}")  # Parámetro de ruta (esta en la url)
async def get_articulos_by_id(id: int):
    for articulo in articulos:
        if articulo["id"] == id:
            return articulo
    return {"detail": "Not found"}


@app.post("/articulos")  # Parámetro query-> /articulos?clave=valor&llave=valor
async def crear_articulo(id: int, nombre: str, precio: float):
    nuevo_articulo = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
    }
    articulos.append(nuevo_articulo)
    return nuevo_articulo

@app.delete("/articulos/{id}")
async def borrar_articulo(id:int):
    for articulo in articulos:
        if articulo["id"] == id:
            articulos.remove(articulo)
            return {"detail":"Borrado correctamente"}
    return {"detail":"no encontrado"}

@app.put("/articulos/{id}")
async def editar_articulo(id:int, nombre:str, precio:float):
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
