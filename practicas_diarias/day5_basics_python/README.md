# 📅 Día 5: Persistencia de Datos y Manejo de Archivos
En este módulo aprendí a dar "memoria" a mis aplicaciones de Python. Ya no solo procesamos datos en la RAM, sino que los guardamos físicamente en el disco duro.

📋 Conceptos Clave
Gestión de Contexto (with open): Aprendí que esta es la forma más segura de abrir archivos, ya que garantiza que el recurso se cierre automáticamente, evitando fugas de memoria o archivos bloqueados.

Modos de Apertura:

'a' (Append): Fundamental para bitácoras y registros. Permite añadir información al final del archivo sin destruir lo existente.

'r' (Read): Para recuperar la información almacenada.

Limpieza de Datos (.strip()): Aprendí la importancia de limpiar los espacios en blanco y saltos de línea (\n) al leer archivos para que la lógica del Backend sea precisa.

🛠️ Lo que implementé
-Desarrollé un Sistema de Convocatoria que:
-Solicita nombres de jugadores por consola.
-Los almacena de forma persistente en un archivo .txt.
-Muestra la lista actualizada leyendo el archivo en tiempo real.
-Utiliza Manejo de Excepciones (try/except) para evitar que el programa falle si el archivo de lectura no existe.