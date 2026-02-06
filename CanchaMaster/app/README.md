# 🏟️ Documentación Técnica: Clase `CanchaDataBase`

Este documento resume los conceptos de SQL y Python aplicados en el archivo `database.py` para el proyecto **Cancha Master**.

---

## 🧠 Glosario de Dudas y Conceptos Clave

### 1. Gestión de Conexiones (`with` + `conectar`)
**Código:** `with self.conectar() as conn:`
* **Significado:** Es un "Gestor de Contexto".
* **Estudio:** Abre la conexión y garantiza que se **cierre automáticamente**. Sin esto, la base de datos podría quedar bloqueada (Locked) si el programa falla.

### 2. Tipos de Datos en SQLite
* **`REAL`**: Se usa para números con decimales (ej: precios `$25.50`). En Python es un `float`.
* **`TEXT`**: Se usa para cadenas de texto y para **Fechas** (formato `YYYY-MM-DD`), ya que SQLite no tiene un tipo `DATE` nativo.
* **`BOOLEAN`**: Internamente SQLite lo guarda como un entero: `0` para Falso y `1` para Verdadero.
* **`DEFAULT`**: Define un valor automático. Ej: `DEFAULT 0` en `pagado` significa que el equipo inicia debiendo hasta que se actualice.



### 3. Blindaje de Datos (`CHECK`)
**Concepto:** Son reglas que impiden guardar información incorrecta.
* **Roles:** `CHECK (rol IN ('admin', 'empleado', 'cliente'))`. Solo permite estos tres valores.
* **Fases:** `CHECK (fase IN ('Octavos', 'Cuartos', 'Semis', 'Final'))`. Asegura que el torneo siga la estructura oficial.

---

## 🏗️ Relaciones y Consultas Pro

### Relaciones (`FOREIGN KEY`)
Permiten conectar tablas. Por ejemplo, en la tabla `jugadores` guardamos el `equipo_id`. Esto evita repetir el nombre del equipo muchas veces y mantiene la integridad: no puedes tener un jugador en un equipo que no existe.

### Consultas con `JOIN` (Unión de Tablas)
En el método `obtener_partidos_por_fase`, usamos `JOIN` para traer nombres reales en lugar de IDs.
* **`JOIN equipos e1 ON p.equipo_local_id = e1.id`**: Busca el nombre del equipo que coincide con el ID del local.



### Parámetros de Seguridad (`?`)
**Código:** `cursor.execute("... VALUES (?, ?)", (nombre, capitan))`
* **Estudio:** El signo `?` es un marcador. **Nunca** concatenamos variables directamente en el texto del SQL para evitar **Inyección SQL** (hackeos).

---

## 🛠️ Estructura de Carpetas Sugerida
Para que el proyecto sea escalable y profesional (Nivel 4to año UTP):
```text
/CanchaMaster
├── app/
│   ├── main.py            # Motor FastAPI (Rutas)
│   └── database.py        # Tu Clase CanchaDataBase
├── templates/             # Interfaz Jinja2 (HTML)
└── static/                # Estilos (Bootstrap/CSS)