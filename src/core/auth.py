import bcrypt

# Funciones utilitarias para la autenticación


def get_password_hash(password: str) -> str:
    """
    Función que a partir de una contraseña en texto plano, genera un hash.
    Convierte el str plano en bytes, genera un salt único y la 'encripta'.
    Devuelve el hash creado a partir de la contraseña. Es lo hay que guardar en la DB.
    """
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()  # Identificador único para generar el hash
    hashed_pwd = bcrypt.hashpw(pwd_bytes, salt).decode("utf-8")
    return hashed_pwd


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Chequea si la contraseña en texto plano coincide con la contraseña hasheada.
    No se 'des-encripta', devuelve True o False.
    """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), hashed_password.encode("utf-8")
    )
