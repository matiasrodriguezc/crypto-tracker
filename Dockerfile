# 1. Usamos Python liviano
FROM python:3.9-slim

# 2. Evitamos que Python guarde archivos .pyc y bufferee la salida
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Carpeta de trabajo adentro del contenedor
WORKDIR /app

# 4. Instalamos dependencias
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el código
COPY app/ .

# No ponemos ENTRYPOINT aquí porque lo definiremos en el docker-compose
# para usar esta misma imagen para la API y el Worker.
