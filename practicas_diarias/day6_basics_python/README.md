📅 Día 6: Bases de Datos Relacionales y Git Flow Profesional
En este módulo di el salto de guardar datos en simples archivos de texto a utilizar un motor de Base de Datos Relacional (SQLite). Además, implementé por primera vez un flujo de trabajo basado en Ramas (Branching), simulando un entorno de desarrollo real.

🗄️ Persistencia con SQLite
A diferencia de los archivos .txt, el uso de una base de datos me permite estructurar la información de manera eficiente y realizar consultas complejas mediante el lenguaje SQL.

SQL implementado:

CREATE TABLE: Definición de la estructura (esquema) para los jugadores.

INSERT: Inserción de registros en la base de datos.

SELECT: Recuperación y visualización de datos desde Python.

Concepto de Primary Key: Implementé un ID único autoincremental para asegurar la integridad de cada registro, un estándar en el desarrollo de Backend.

🌿 Git Flow: Trabajando en Ramas
Para este desafío, dejé de trabajar directamente en la rama main y seguí el estándar de la industria:

Feature Branch: Creé la rama feature/mi-primera-db para desarrollar la funcionalidad de forma aislada.

Pull Request (PR): Utilicé la interfaz de GitHub para comparar mis cambios y asegurar que el código fuera estable.

Merge: Integré los cambios exitosamente a la carretera principal (main) tras verificar que todo funcionaba correctamente.

🛠️ Tecnologías Utilizadas
Python: Lógica de conexión y manipulación de datos.

SQLite3: Motor de base de datos ligero y potente.

Git: Control de versiones avanzado (branch, checkout, merge, pull).

GitHub Actions: Mi "robot" de CI que validó que el código de la base de datos no tuviera errores de sintaxis.