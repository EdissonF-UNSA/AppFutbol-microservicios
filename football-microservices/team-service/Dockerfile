# Utilizamos una imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos las dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiamos el código fuente
COPY ./app /app

# Exponemos el puerto que usará FastAPI
EXPOSE 8000

# Comando para ejecutar el servicio con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
