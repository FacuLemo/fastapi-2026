from fastapi import APIRouter

saludar_routers = APIRouter()


@saludar_routers.get("/")
def saludo():
    return "hola"
