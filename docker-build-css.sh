#!/bin/bash

# Instalar dependencias de Node.js si es necesario
echo "Instalando dependencias de Node.js..."
docker-compose exec web npm install

# Compilar Tailwind CSS
echo "Compilando Tailwind CSS..."
docker-compose exec web npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css

# Ejecutar collectstatic para recopilar archivos estáticos
echo "Recopilando archivos estáticos..."
docker-compose exec web python manage.py collectstatic --noinput

# Comprimir archivos estáticos
echo "Comprimiendo archivos estáticos..."
docker-compose exec web python manage.py compress --force

echo "¡Proceso completado con éxito!" 