#!/bin/bash

set -o errexit  
set -o pipefail  
set -o nounset

# Instalar dependencias de Node.js
echo "Instalando dependencias de Node.js..."
npm install

# Compilar Tailwind CSS
echo "Compilando Tailwind CSS..."
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css

# Collect static files
echo "Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Comprimir archivos estáticos
echo "Comprimiendo archivos estáticos..."
python manage.py compress --force

# Run database migrations
echo "Ejecutando migraciones de la base de datos..."
python manage.py migrate --noinput

# Determinar si está en modo desarrollo o producción
if [ "${DJANGO_DEBUG:-false}" = "true" ]; then
    echo "Ejecutando en modo desarrollo con recarga automática"
    python manage.py runserver 0.0.0.0:8000
else
    echo "Ejecutando en modo producción con Gunicorn"
    # Start Gunicorn
    gunicorn agro_veterinaria.wsgi:application --bind 0.0.0.0:8000
fi