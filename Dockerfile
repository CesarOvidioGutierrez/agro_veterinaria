# Dockerfile
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv

# Instalar Node.js y npm
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Crear y activar entorno virtual
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set work directory
WORKDIR /app

COPY requirements.txt .

# Instalar dependencias en el entorno virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

ENTRYPOINT [ "/bin/bash" ]
CMD ["/app/docker-entrypoint.sh"]
