## Instalación del proyecto
Clonan el repositorio desde el ssh (Deberán tener configurado git en sus máquinas)
Una vez clonado, creamos y activamos el entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```
Instalamos FastAPI **a partir del requirements**
```
pip install -r requirements.txt
```
Iniciamos FastAPI
```
fastapi dev src/main.py
```
## Otros comandos útiles
para instalar la última versión de FastAPI
```bash
pip install fastapi"[standard]"
```
Para crear requirements (asegúrense de estar dentro del entorno virtual)
```bash
pip freeze > requirements.txt
```

