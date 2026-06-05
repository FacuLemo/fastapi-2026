from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.articulos import articulos_routers
from routers.saludar import saludar_routers

app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

#Inclumos los routers (path operations)

app.include_router(articulos_routers, tags=["Artículos"], prefix="/articulos")
app.include_router(saludar_routers, tags=["Saludos"], prefix="/saludos")

#^ Tags agrupa en la documentación
#^ Prefix le pone prefijos a las urls de cada path operation definido en ese router


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
