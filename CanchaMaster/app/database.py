import sqlite3
import os

class CanchaDataBase:
    def __init__(self, db_name="canchamaster.db"):
        self.ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)
        self.crear_tablas()
        
    def conectar(self):
        return sqlite3.connect(self.ruta)
    
    def crear_tablas(self):
        with self.conectar() as conn:
            cursor = conn.cursor()
            # 1. EQUIPOS
            cursor.execute('''CREATE TABLE IF NOT EXISTS equipos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE,
                capitan TEXT,
                pagado BOOLEAN DEFAULT 0
            )''')
            # 2. JUGADORES
            cursor.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                posicion TEXT,
                equipo_id INTEGER,
                FOREIGN KEY (equipo_id) REFERENCES equipos (id)
            )''')
            # 3. CANCHAS
            cursor.execute('''CREATE TABLE IF NOT EXISTS canchas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tipo TEXT CHECK (tipo IN ('5vs5', '7vs7')), 
                precio_hora REAL
            )''')
            # 4. RESERVAS (Asegúrate que el nombre de la columna sea 'cliente')
            cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cancha_id INTEGER,
                cliente TEXT, 
                fecha TEXT,
                hora TEXT,
                total_a_pagar REAL,
                monto_pagado REAL DEFAULT 0,
                FOREIGN KEY (cancha_id) REFERENCES canchas (id)
            )''')
            # 5. PARTIDOS
            cursor.execute('''CREATE TABLE IF NOT EXISTS partidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                equipo_local_id INTEGER,
                equipo_visitante_id INTEGER,
                goles_local INTEGER DEFAULT 0,
                goles_visitante INTEGER DEFAULT 0,
                fase TEXT CHECK (fase IN ('Octavos', 'Cuartos', 'Semis', 'Final')), 
                estado TEXT DEFAULT 'Pendiente' CHECK (estado IN ('Pendiente', 'Finalizado')),
                fecha TEXT,
                FOREIGN KEY (equipo_local_id) REFERENCES equipos (id),
                FOREIGN KEY (equipo_visitante_id) REFERENCES equipos (id)
            )''')
            # 6. USUARIOS
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                rol TEXT DEFAULT 'empleado' CHECK (rol IN ('admin', 'empleado', 'cliente'))
            )''')
            conn.commit()

    # --- MÉTODOS DE INSCRIPCIÓN Y CONSULTA ---

    def inscribir_equipo(self, nombre, capitan, pagado=0):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO equipos (nombre, capitan, pagado) VALUES (?, ?, ?)", 
                           (nombre, capitan, pagado))
            conn.commit()

    def obtener_partidos_por_fase(self, fase_buscada):
        """Une las tablas de partidos y equipos para mostrar nombres reales"""
        query = '''
            SELECT p.id, e1.nombre, e2.nombre, p.goles_local, p.goles_visitante, p.estado
            FROM partidos p
            JOIN equipos e1 ON p.equipo_local_id = e1.id
            JOIN equipos e2 ON p.equipo_visitante_id = e2.id
            WHERE p.fase = ?
        '''
        with self.conectar() as conn:
            return conn.execute(query, (fase_buscada,)).fetchall()

    def obtener_deudores(self):
        """Calcula deudas comparando el total con lo pagado"""
        query = """
            SELECT cliente, (total_a_pagar - monto_pagado) AS saldo_pendiente, fecha
            FROM reservas
            WHERE monto_pagado < total_a_pagar
        """
        with self.conectar() as conn:
            return conn.execute(query).fetchall()

    def guardar_partido_sorteado(self, id_local, id_visitante, fase):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO partidos (equipo_local_id, equipo_visitante_id, fase) 
                VALUES (?, ?, ?)
            ''', (id_local, id_visitante, fase))
            conn.commit()

    def inicializar_negocio(self):
        """Inserta las canchas iniciales si la tabla está vacía"""
        canchas_iniciales = [
            ('Cancha Central', '5vs5', 25.00),
            ('Cancha Norte', '5vs5', 25.00),
            ('Estadio 7', '7vs7', 40.00)
        ]
        with self.conectar() as conn:
            cursor = conn.cursor()
            # Solo insertamos si no hay canchas registradas
            cursor.execute("SELECT COUNT(*) FROM canchas")
            if cursor.fetchone()[0] == 0:
                cursor.executemany(
                    "INSERT INTO canchas (nombre, tipo, precio_hora) VALUES (?, ?, ?)",
                    canchas_iniciales
                )
                conn.commit()
                print("✅ Canchas del negocio inicializadas.")