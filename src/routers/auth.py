from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from core.auth import get_password_hash, verify_password
from database import get_db
from models.usuarios import Usuario, UsuarioCreate, UsuarioLogin, UsuarioPublic

auth_routers = APIRouter()


@auth_routers.post(
    "/register", response_model=UsuarioPublic
)  # REGISTER: CREACIÓN DE MODELO USUARIO
async def register(usuario_nuevo: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = Usuario.model_validate(usuario_nuevo)

    # Lógica de encriptación (hasheo) de contraseña
    usuario_db.contraseña = get_password_hash(usuario_nuevo.contraseña)

    db.add(usuario_db)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db


@auth_routers.post("/login")
async def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    #SIN TERMINAR
    query = select(Usuario).where(Usuario.email == usuario.email)
    usuario_db = db.exec(query).first()

    resultado = verify_password(usuario.contraseña, usuario_db.contraseña)
    #Idealmente, si coincide, generar y devolver el JWT Token (contexto de login)
    return {"coincide": resultado}
