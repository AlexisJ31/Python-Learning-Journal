# importarmos la libreria sqlite3 para manejar la base de datos SQLite
import sqlite3
import os
# definimos la ruta de la base de datos
ruta_db = os.path.join(os.path.dirname(__file__), "registro.db")
# funcion para crear la tabla de registros si no existe
def crear_tabla():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            posicion TEXT,
            edad INTEGER,
            equipo boolean
        )
    ''')
    conexion.commit()
    conexion.close()
# creamos otra tabla para los marcadores
def crear_tabla_marcadores():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS marcadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            equipo_local TEXT NOT NULL,
            equipo_visitante TEXT NOT NULL,
            goles_local INTEGER,
            goles_visitante INTEGER,
            fecha_partido DATE
        )
    ''')
    conexion.commit()
    conexion.close()    

# funcion para agregar un jugador a la base de datos
def agregar_jugador(nombre, posicion, edad, equipo):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO jugadores (nombre, posicion, edad, equipo)
        VALUES (?, ?, ?, ?)
    ''', (nombre, posicion, edad, equipo))
    conexion.commit()
    conexion.close()

# funcion para ver los jugadores en la base de datos
def ver_jugadores():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM jugadores')
    jugadores = cursor.fetchall()
    for jugador in jugadores:
        print(f"ID: {jugador[0]}, Nombre: {jugador[1]}, Posicion: {jugador[2]}, Edad: {jugador[3]}, Equipo: {jugador[4]}")
    conexion.close()

# funcion para ingresar el marcador de un partido
def agregar_marcador(equipo_local, equipo_visitante, goles_local, goles_visitante, fecha_partido):
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO marcadores (equipo_local, equipo_visitante, goles_local, goles_visitante, fecha_partido)
        VALUES (?, ?, ?, ?, ?)
    ''', (equipo_local, equipo_visitante, goles_local, goles_visitante, fecha_partido))
    conexion.commit()
    conexion.close()

# funcion para ver el marcador de los partidos
def ver_marcadores():
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM marcadores')
    marcadores = cursor.fetchall()
    for marcador in marcadores:
        print(f"ID: {marcador[0]}, Equipo Local: {marcador[1]}, Equipo Visitante: {marcador[2]}, Goles Local: {marcador[3]}, Goles Visitante: {marcador[4]}, Fecha Partido: {marcador[5]}")
    conexion.close()

# llamamos a la funcion para crear las tablas al inicio
crear_tabla()