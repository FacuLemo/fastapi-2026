## Instalación del proyecto
Clonan el repositorio desde el ssh (Deberán tener configurado git en sus máquinas)
Una vez clonado, creamos y activamos el entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```
> Altenativamente podemos usar un gestor de entornos virtuales como [uv](https://docs.astral.sh/uv/)

Una vez dentro del entorno virtual, instalamos FastAPI **a partir del requirements**
```
pip install -r requirements.txt
```

Iniciamos FastAPI
```
fastapi dev src/main.py
```

Finalmente, para levantar la base de datos debemos correr un comando de Alembic:
```bash
alembic upgrade head
```

## Otros comandos útiles

### Sobre el entorno virtual
para instalar la última versión de FastAPI
```bash
pip install fastapi"[standard]"
```
Para crear requirements (asegúrense de estar dentro del entorno virtual)
```bash
pip freeze > requirements.txt
```
---
### Comandos para UV (gestor de entornos virtuales)

Inicializa un nuevo proyecto con:
```shell
uv init Proyecto-fastapi
```

Entrá a la carpeta que acabás de crear (con `cd Proyecto-fastapi`). Una vez dentro, Instala fastapi:
```bash
uv add fastapi[standard]
```

Luego para levantar fastapi
```bash
uv run fastapi dev
```
> "uv run" permite correr cualquier comando, por ejemplo para ejecutar migraciones tenés que hacer `uv run alembic upgrade head`

---

* Para Congelar versiones (equivalente a freeze): `uv lock` 

* Sincronizar entorno (instalar dependencias): `uv sync`

* Para instalar dependencias desde requirements: `uv add -r requirements.txt`
