from fastapi import FastAPI
import requests 
# Importamos la función que ya creaste en tu otro archivo
from prueba_final_semana1.conexion_bd import crear_tabla 

app = FastAPI()

@app.get("/")
def home():
    return {"status": "API Corriendo", "clase": "UTP Software Development"}

@app.get("/inicializar-db")
def setup():
    # Usamos la función que ya tenías hecha
    crear_tabla()
    return {"mensaje": "Base de datos preparada usando tu código previo"}

# Añade esto debajo de tu ruta @app.get("/")
@app.get("/jugador-estrella")
def get_estrella():
    return {
        "nombre": "Einar",
        "posicion": "Contención",
        "equipo": "UTP FC",
        "estado": "Entrenando para el torneo"
    }



@app.get("/jugadores-pro")
def traer_jugadores_internet():
    # Esta es una URL de prueba con datos reales de internet
    url = "https://jsonplaceholder.typicode.com/users"
    
    respuesta = requests.get(url)
    datos = respuesta.json() # Convertimos lo que nos mandan a formato Python
    
    # Vamos a filtrar solo los nombres para que no sea un desorden
    nombres = [usuario["name"] for usuario in datos]
    
    return {"jugadores_mundiales": nombres}