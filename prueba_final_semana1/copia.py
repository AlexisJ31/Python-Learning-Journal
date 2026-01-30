#creamo los import necesarios
import os
#definimos la funcion para agregar jugador
def ruta_origen(nombre, posicion, dorsal):
    # definimos la ruta del archivo de copia
    ruta_log = os.path.join(os.path.dirname(__file__), "torneo.txt")
    # abrimos el archivo udsando "a" para agregar contenido al final del archivo y whith para asegurar el cierre del archivo
    with open(ruta_log, "a") as archivo:
        archivo.write(f"[Registro]: {nombre}, posicion: {posicion}, dorsal: {dorsal}\n")