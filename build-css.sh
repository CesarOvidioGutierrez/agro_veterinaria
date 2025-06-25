#!/bin/bash

# Compilar Tailwind CSS
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css

# Ejecutar collectstatic para recopilar archivos estáticos
python manage.py collectstatic --noinput

# Comprimir archivos estáticos
python manage.py compress --force 