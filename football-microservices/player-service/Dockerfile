# Utiliza una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de dependencias y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación
COPY ./app /app

# Copiamos el directorio 'static' al contenedor
COPY ./static /app/static

# Exponemos el puerto en el que la aplicación se ejecutará
EXPOSE 8000

# Comando para ejecutar el servidor con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
