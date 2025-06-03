#!/bin/bash

set -o errexit  
set -o pipefail  
set -o nounset

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations
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