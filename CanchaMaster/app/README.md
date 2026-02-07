# 🏟️ Proyecto Cancha Master

Bienvenido al centro de control del proyecto. Aquí documento todo mi progreso, desde los datos hasta la interfaz web.

---
## 🏗️ PARTE 1: El Motor (Base de Datos)
### 🧠 Glosario de Dudas y Conceptos Clave

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
## 🌐 PARTE 2: El Rostro (FastAPI y Vistas)
# 📓 Mi Diario de Programación: El Enredo de las Vistas 🏟️

Este documento es para recordar cómo logramos que la aplicación **Cancha Master** dejara de ser solo texto y se convirtiera en una página web real. ¡Fue un dolor de cabeza, pero aquí está la solución!

---

## 🚦 1. El Héroe del día: El módulo `os`
**¿Qué es?** Es una herramienta de Python para hablar con el Sistema Operativo (Windows en este caso).
**¿Por qué lo usamos?** Porque antes le decíamos a Python: "Busca la carpeta de las páginas ahí mismo". Pero si tú lanzabas el programa desde otra carpeta, Python se perdía.

* **La solución:** Usamos `os.path.join` y `__file__`.
* **En español:** Esto le dice a Python: "No importa dónde estés, busca donde está guardado este archivo, camina hacia la carpeta `app` y entra en `template`". ¡Santo remedio para los errores de rutas!



---

## ❌ 2. El "Muro" del Error 500 (Internal Server Error)
Si ves este error en el navegador, ¡no entres en pánico! Generalmente es por una de estas dos tonterías:

1.  **El Plural Traicionero:** Yo tenía la carpeta llamada `template` (singular), pero en el código escribí `templates` (plural). Para la computadora, son dos galaxias distintas. **Lección:** Revisa letra por letra los nombres de tus carpetas.
2.  **El Import "Metiche":** El programa que usamos para escribir código (VS Code) a veces intenta ayudarnos y trae herramientas que no son. Trajo un `Request` que era para descargar cosas de internet, cuando nosotros necesitábamos el de **FastAPI** para mostrar la página.

---

## 🖼️ 3. ¿Cómo funciona la "Vista" (Jinja2)?
Para que Alexis vea su nombre en la pantalla, usamos un "traductor" llamado **Jinja2**.

* **El Mensajero (`Request`):** Es obligatorio ponerlo. Es como el cartero que lleva la información del usuario al servidor.
* **El Diccionario (`context`):** Es una cajita donde metemos los datos de Python. Por ejemplo: `{"mensaje": "Hola Alexis"}`.
* **Las Llaves Mágicas `{{ }}`:** En el archivo HTML, si ponemos `{{ mensaje }}`, Jinja2 lo cambia por el texto real que definimos en Python.



---

## 🛠️ Comandos de "Rescate" (Para estudiar)

Si el servidor se queda trabado o no reconoce los cambios, seguir pasos:

1.  **Matar el proceso:** Presiona `Ctrl + C` en la terminal. Es como apagar y prender el router.
2.  **El comando maestro:** `uvicorn app.main:app --reload --port 8005`
    * `app.main`: Entra a la carpeta `app` y busca `main.py`.
    * `--reload`: Se actualiza solo cada vez que das "Guardar".
    * `--port 8005`: Cambiamos de puerta para que no choque con otros proyectos viejos.

---
## 💡 Consejo para el "Alexis del Futuro"
Si algo no carga, primero mira la terminal (la pantallita negra). Si ves un texto rojo que dice `TemplateNotFound`, es que escribiste mal el nombre de la carpeta o del archivo `.html`. **¡Las rutas lo son todo!**

## 🛠️ Estructura de Carpetas Sugerida
Para que el proyecto sea escalable y profesional (Nivel 4to año UTP):
```text
/CanchaMaster
├── app/
│   ├── main.py            # Motor FastAPI (Rutas)
│   └── database.py        # Tu Clase CanchaDataBase
├── templates/             # Interfaz Jinja2 (HTML)
└── static/                # Estilos (Bootstrap/CSS)
---

## 🛠️ Cómo correr este proyecto
Para que no se me olvide la ruta después:
1. Abrir terminal en la carpeta raíz.
2. Comando: `uvicorn app.main:app --reload --port 8005`