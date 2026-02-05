# 1. Imagen base de Python (ligera)
FROM python:3.10-slim

# 2. Evita que Python genere archivos .pyc y permite ver logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiamos todo tu repositorio al contenedor
COPY . .

# 5. Comando para ejecutar tu aplicación (Ajusta la ruta si es necesario)
# Si tu archivo principal está en la carpeta del día 7, la ruta sería:
CMD ["python", "practicas_diarias/day7_final_challenge/interface.py"]