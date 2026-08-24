from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.articulos import Articulo #IMPORTANTE para que se cree la tabla, aunque no se use en código
from database import Base, engine
from routers.articulos import articulos_routers
from routers.saludar import saludar_routers

# Crea las tablas y la db
Base.metadata.create_all(bind=engine)

# Fastapi -> Framework para hacer APIs
# Framework -> marco de trabajo -> herramientas y formas de trabajar para cumplir un próposito
# instalamos creando un entorno virtual: python3 -m venv venv
# activamos: source... pip install ... pip freeze....
# y finalmente: fastapi dev
# ...
# Gestores de entornos virtuales -> uv de Astral:
# uv init proyecto-FastAPI && cd proyecto-FastAPI
# uv add FastAPI --extra standard
# uv run fastapi dev


# CRUD EN MEMORIA -> VOLATIL -> simulo una db que no persiste
# CREATE
# READ
# UPDATE
# DELETE


# API -> PROTOCOLO HTTP
# Requests & Responses

# Cliente usa request (peticiones)

# 1 ELEMENTO DE LA REQUEST: MÉTODOS HTTP
# POST -> PUBLICAR/CREAR/AGREGAR UN DATO
# GET -> OBTENER UN DATO
# PUT -> ACTUALIZAR/EDITAR UN DATO COMPLETO
# PATCH -> ACTUALIZAR/EDITAR UN DATO PARCIAL
# DELETE -> BORRAR UN DATO
# cada uno corresponde a una operacion CRUD

# 2 ELEMENTO REQUEST: ENDPOINT/URL/PATH
# GET https://localhost:8000/articulo

# 3 ELEMENTO: BODY json
# POST https://localhost:8000/articulo {"nombre":"articulo1", "precio":500}

# RESPONSE (Respuesta)
# 1 ELEMENTO: BODY
# {"MENSAJE":"ARTICULO CREADO"}

# 2 ELEMENTO: STATUS CODE -> van del 100 al 500
# 200 -> OK (SALIO TODO BIEN)
# 500 -> ERROR DE PROGRAMACION/SERVIDOR
# 400 -> ERROR DEL LADO DEL CLIENTE


app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

# Inclumos los routers (path operations)

app.include_router(articulos_routers, tags=["Artículos"], prefix="/articulos")
app.include_router(saludar_routers, tags=["Saludos"])

# ^ Tags agrupa en la documentación
# ^ Prefix le pone prefijos a las urls de cada path operation definido en ese router


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
