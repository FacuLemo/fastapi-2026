from fastapi import APIRouter, Depends

# Ahora que usamos sqlmodel no traemos nada de sqlalchemy.
from sqlmodel import Session, select

from database import get_db
from models.anidados import ProveedorNested

# Y también nuestros schemas son los models. (fíjense los response_model)
from models.proveedor import Proveedor, ProveedorBase, ProveedorPublic

proveedor_routers = APIRouter()

# --------------


@proveedor_routers.get("/", response_model=list[ProveedorNested])
async def get_(db: Session = Depends(get_db)):  # Inyección de Dependencias
    articulos = db.exec(select(Proveedor)).all()
    return articulos


@proveedor_routers.post(
    "/proveedor", response_model=ProveedorPublic
)  # parametro query -> endpoint?clave=valor&otra_clave=valor
async def crear_proveedor(proveedor: ProveedorBase, db: Session = Depends(get_db)):
    # proveedors
    nuevo_prove = Proveedor.model_validate(proveedor)

    db.add(nuevo_prove)
    db.commit()
    db.refresh(nuevo_prove)
    return nuevo_prove
