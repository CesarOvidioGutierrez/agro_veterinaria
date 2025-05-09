### README

# Proyecto Agro Veterinaria con Django 4.2

Este proyecto es una aplicación para gestión de productos y servicios agro veterinarios usando Django 4.2, Docker, Docker Compose y Nginx.

## Requisitos Previos

- Docker: [Instalar Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Configuración

### Docker Compose

El archivo `docker-compose.yml` define tres servicios:

- **db**: Servicio de base de datos PostgreSQL.
- **web**: Servicio de aplicación Django.
- **nginx**: Servicio Nginx para manejar peticiones HTTP.

### Dockerfile

El `Dockerfile` define el entorno para la aplicación Django:

- Usa la imagen base `python:3.10-slim`.
- Crea un entorno virtual Python en `/opt/venv`.
- Establece el directorio de trabajo a `/app`.
- Instala las dependencias de `requirements.txt` en el entorno virtual.
- Copia todos los archivos al contenedor.
- Define el script de entrada (`docker-entrypoint.sh`).

## Cómo Configurar el Entorno

### 1. Clonar el Repositorio

```sh
git clone https://github.com/your-username/agro_veterinaria.git
cd agro_veterinaria
```

### 2. Construir Imágenes Docker

Antes de iniciar los servicios, necesitas construir las imágenes Docker con el siguiente comando:

```sh
docker compose build
```

### 3. Iniciar los Servicios

Una vez que las imágenes están construidas, puedes iniciar todos los servicios con:

```sh
docker compose up
```

Este comando iniciará los contenedores para la base de datos PostgreSQL, la aplicación Django y Nginx. Puedes acceder a la aplicación en:
- http://localhost - A través de Nginx
- http://localhost:8000 - Directamente al servidor de desarrollo Django (con recarga automática)

### 4. Modo de Desarrollo con Recarga Automática

El proyecto está configurado para funcionar en modo desarrollo, lo que permite:
- Ver cambios en tiempo real sin reconstruir la imagen
- Crear nuevas apps de Django o modificar módulos existentes
- Recarga automática del servidor cuando detecta cambios en el código

Para activar/desactivar este modo, modifica la variable `DJANGO_DEBUG` en el archivo `docker-compose.yml`:
```yaml
environment:
  - DJANGO_DEBUG=true  # 'true' para desarrollo, 'false' para producción
```

## Desarrollo con Django en Docker

### Crear una Nueva App de Django

Para crear una nueva aplicación Django en el proyecto, ejecuta:

```sh
docker compose exec web python manage.py startapp nombre_app
```

Este comando creará una nueva carpeta con la estructura básica de una app Django directamente en tu directorio local (gracias al volumen montado).

El entorno virtual está siempre activado dentro del contenedor, por lo que no necesitas activarlo manualmente.

### Otros Comandos Comunes de Django

Todos los comandos de Django se pueden ejecutar dentro del contenedor:

```sh
# Crear migraciones
docker compose exec web python manage.py makemigrations

# Aplicar migraciones
docker compose exec web python manage.py migrate

# Crear superusuario
docker compose exec web python manage.py createsuperuser

# Abrir shell de Django
docker compose exec web python manage.py shell
```

### 5. Archivos Estáticos y Migraciones

El script `docker-entrypoint.sh` ya está configurado para ejecutar automáticamente:
- Recolección de archivos estáticos
- Migraciones de base de datos

Si necesitas ejecutar estos comandos manualmente:

```sh
docker compose run web python manage.py collectstatic --noinput
docker compose run web python manage.py migrate
```

## Comandos Útiles de Docker

- **Iniciar servicios en segundo plano:**

  ```sh
  docker compose up -d
  ```

- **Detener servicios:**

  ```sh
  docker compose down
  ```

- **Ver logs de un servicio específico:**

  ```sh
  docker compose logs <nombre_servicio>
  ```

- **Acceder a un contenedor en ejecución:**

  ```sh
  docker compose exec <nombre_servicio> /bin/bash
  ```

  Nota: Para el servicio Nginx, use sh en lugar de bash:

  ```sh
  docker compose exec nginx sh
  ```

- **Instalar una nueva dependencia Python:**

  ```sh
  docker compose exec web pip install nombre_paquete
  ```
  Y luego añadirla a requirements.txt para que se instale en futuras construcciones

## Entorno Virtual en Docker

El proyecto utiliza un entorno virtual Python dentro del contenedor Docker para una mayor consistencia con prácticas de desarrollo estándar. Esto proporciona:

- Aislamiento de dependencias similar al desarrollo local
- Consistencia en las rutas de instalación de paquetes
- Compatibilidad con herramientas que esperan un entorno virtual

## Estructura de Archivos

- `agro_veterinaria/`: Contiene la configuración principal del proyecto Django
- `requirements.txt`: Lista de dependencias Python (Django 4.2, etc.)
- `Dockerfile`: Configuración para crear la imagen Docker
- `docker-compose.yml`: Orquestación de los servicios
- `nginx.conf`: Configuración del servidor Nginx
- `docker-entrypoint.sh`: Script de inicio para el contenedor web

## Notas

- Asegúrate de que los archivos `requirements.txt`, `nginx.conf` y `docker-entrypoint.sh` estén en el directorio raíz del proyecto.
- Modifica las configuraciones según sea necesario para tu entorno de desarrollo.

¡Y eso es todo! Ahora tienes un entorno Django 4.2 completamente funcional usando Docker, con soporte para desarrollo con recarga automática.
