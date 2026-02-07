#este sera el cerebro de mi app
# importamos todo lo necesario
import os
#importe de FastAPI
from fastapi import FastAPI, Request
#importamos jinja2 para renderizar las plantillas HTML
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
#importamos la base de datos
from app.database import CanchaDataBase

#creamos las respectivas variables que usare
app = FastAPI()
db = CanchaDataBase()

# Detectamos la ruta absoluta de la carpeta 'app'
base_path = os.path.dirname(__file__)
# Unimos la ruta de 'app' con la carpeta 'template' (fíjate que no tiene S)
templates = Jinja2Templates(directory=os.path.join(base_path, "template"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request): 
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "mensaje": "¡Bienvenido a Cancha Master, Alexis!"
    })