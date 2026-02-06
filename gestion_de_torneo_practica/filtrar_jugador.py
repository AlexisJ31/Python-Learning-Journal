import sqlite3
import os
ruta_db = os.path.join(os.path.dirname(__file__), "registro.db")
#filtramos jugador por posicion
def filtrar_jugador_por_posicion(posicion_buscada):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM jugadores WHERE posicion = ?', (posicion_buscada,))
    jugadores_filtrados = cursor.fetchall()
    if not jugadores_filtrados:
        print(f"No se encontraron jugadores con la posición '{posicion_buscada}'")
    else:
        for jugador in jugadores_filtrados:
            # Corrige el print para que sea coherente con tu tabla:
            print(f"ID: {jugador[0]}, Nombre: {jugador[1]}, Posicion: {jugador[2]}, Edad: {jugador[3]}")