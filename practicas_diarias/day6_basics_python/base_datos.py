import sqlite3
import os
# Esto asegura que la base de datos se cree en la misma carpeta que el script
ruta_db = os.path.join(os.path.dirname(__file__), "torneo.db")
# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect(ruta_db)
# lo que hace el cursor es para escribir y ejecutar comandos SQL
cursor = conexion.cursor()
# Crear la tabla de jugadores si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        posicion TEXT,
        goles INTEGER DEFAULT 0
    )
''')
# insertamos un jugador de ejemplo
cursor.execute('''
    INSERT INTO jugadores (nombre, posicion, goles)
    VALUES (?, ?, ?)
''', ("Lionel Messi", "Delantero", 30))
# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
# imprimimos un mensaje de confirmación
print("Base de datos y tabla de jugadores creadas correctamente, y jugador de ejemplo insertado.")