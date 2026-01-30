import sqlite3
import os

ruta_db = os.path.join(os.path.dirname(__file__), "torneo.db")

def crear_tabla():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            posicion TEXT,
            dorsal INTEGER
        )
    ''')
    conexion.commit()
    conexion.close()

def agregar_jugador(nombre, posicion, dorsal):
    conexion = sqlite3.connect(ruta_db) # Abres aquí
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO jugadores (nombre, posicion, dorsal)
        VALUES (?, ?, ?)
    ''', (nombre, posicion, dorsal))
    conexion.commit() # Guardas
    conexion.close()  # Cierras aquí

def ver_jugadores():
    conexion = sqlite3.connect(ruta_db) # Abres aquí también
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM jugadores')
    jugadores = cursor.fetchall()
    for jugador in jugadores:
        print(f"ID: {jugador[0]}, Nombre: {jugador[1]}, Posicion: {jugador[2]}, Dorsal: {jugador[3]}")
    conexion.close() # Cierras

# Llamamos a crear_tabla una vez al inicio para asegurar que la DB existe
crear_tabla()