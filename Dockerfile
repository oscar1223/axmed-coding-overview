# Dockerfile

# Imagen base
FROM python:3.9-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Ejecutar migraciones y recolectar archivos estáticos
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "axmed_project.wsgi:application", "--bind", "0.0.0.0:8000"]
