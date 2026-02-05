# 🐍 Python Learning Journal - Alexis Aimar

## 📝 Descripción del Proyecto
Este repositorio es mi bitácora personal de aprendizaje en el lenguaje Python, desarrollada durante mi cuarto año de la carrera de **Desarrollo de Software en la UTP**. El proyecto ha evolucionado desde scripts básicos de lógica hasta una arquitectura de API moderna y profesional.

## 🚀 Funcionalidades Principales
- **Lógica de Programación**: Estructuras de control, ciclos (For/While) y manejo de diccionarios.
- **Persistencia de Datos**: Gestión de archivos `.txt` y bases de datos relacionales con **SQLite**.
- **Arquitectura API REST**: Servidor web interactivo para exponer datos al exterior.
- **Consumo de Servicios**: Integración con APIs externas para obtener información en tiempo real.
- **Pruebas Automatizadas**: Validación de lógica mediante **Pytest**.

## 🏗️ Arquitectura del Sistema
El proyecto está organizado siguiendo estándares de la industria:
1. **Core Logic**: Módulos diarios de práctica (Día 1 al Día 6).
2. **Backend API**: Construido con **FastAPI** para la gestión de solicitudes.
3. **Servidor Intermediario**: Implementación de **Uvicorn** para la ejecución del servicio.
4. **Base de Datos**: Almacenamiento local mediante SQLite para la gestión de torneos de fútbol.
5. **Contenedores**: Empaquetado de la aplicación mediante **Docker** para asegurar portabilidad.

## 📁 Estructura del Repositorio
```text
/
├── backend/          # API principal y lógica de servidor
├── database/         # Archivos .db y scripts de conexión SQL
├── day1_to_day6/     # Prácticas diarias de lógica y archivos
├── tests/            # Pruebas unitarias automatizadas
├── Dockerfile        # Configuración para despliegue en contenedores
├── .gitignore        # Archivos excluidos del control de versiones
└── requirements.txt  # Dependencias del proyecto
```
🛠️ Tecnologías Utilizadas
Backend & API
Python 3.10+ - Lenguaje principal.

FastAPI - Framework moderno para la creación de APIs.

Uvicorn - Servidor ASGI de alto rendimiento.

Requests - Consumo de datos de servidores externos.

DevOps & Calidad
Docker - Virtualización de aplicaciones.

Pytest - Framework de pruebas unitarias.

Git/GitHub - Control de versiones y Git Flow.

GitHub Actions - Integración Continua (CI).

🔧 Instalación y Configuración
Requisitos Previos
Python instalado y entorno virtual (.venv) activado.
