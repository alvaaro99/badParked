# BadParked

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**BadParked** es una aplicación backend en desarrollo que permite a los usuarios gestionar vehículos mal aparcados y notificar al propietario si el vehículo está causando molestias. Los usuarios pueden registrar varios vehículos, activar la visibilidad de su información de contacto cuando el vehículo está mal aparcado, y generar un código QR para facilitar la comunicación con quienes necesiten contactarlos.

## Tabla de Contenidos

-   [Estado del Proyecto](#estado-del-proyecto)
-   [Tecnologías Utilizadas](#tecnologías-utilizadas)
-   [Instalación](#instalación)
-   [Uso](#uso)
-   [Autenticación y Seguridad](#autenticación-y-seguridad)
-   [Generación de Códigos QR](#generación-de-códigos-qr)
-   [Documentación](#documentación)
-   [Licencia](#licencia)

## Estado del Proyecto

BadParked está actualmente en desarrollo y es una aplicación de prueba sin frontend. El proyecto incluye un backend funcional y un endpoint de documentación OpenAPI para ver los endpoints disponibles.

## Tecnologías Utilizadas

-   **Lenguaje**: Python
-   **Frameworks**: FastAPI, SQLModel
-   **Base de Datos**: PostgreSQL (Docker)
-   **Control de Versiones de la BD**: Alembic
-   **Autenticación**: JWT
-   **Seguridad**: Contraseñas almacenadas como hash
-   **Generación de Códigos QR**: Librería `qrcode`

## Instalación

Para instalar y ejecutar BadParked en tu entorno local, sigue los pasos a continuación:

```bash
# Clona el repositorio
git clone https://github.com/tu-usuario/BadParked.git

# Entra en el directorio del proyecto
cd BadParked

# Crea un entorno virtual (opcional pero recomendado)
python3 -m venv venv

# Activa el entorno virtual
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt

# Configura y ejecuta Docker para PostgreSQL
docker-compose up -d

# Realiza las migraciones de la base de datos con Alembic
alembic upgrade head

# Ejecuta la aplicación
fastapi dev src/main.py
```

## Uso

BadParked proporciona una serie de endpoints para gestionar usuarios y vehículos. Puedes acceder a la documentación completa de la API a través de la URL /docs cuando el servidor esté en funcionamiento.

## Autenticación y Seguridad

### Autenticación

Los usuarios se autentican utilizando JWT. Los tokens se generan al iniciar sesión y son necesarios para acceder a la mayoría de los endpoints.

### Contraseñas

Las contraseñas se almacenan como hashes en la base de datos para garantizar la seguridad.

### Generación de Códigos QR

La aplicación permite a los usuarios generar códigos QR utilizando la librería qrcode. Estos códigos contienen una URL que dirige a una página con la información de contacto del propietario del vehículo. Los códigos QR se generan y guardan como archivos PNG dentro del proyecto.

## Documentación

Puedes acceder a la documentación de la API a través de los siguientes endpoints cuando la aplicación esté en funcionamiento:

/docs - Documentación interactiva con Swagger UI

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para obtener más detalles.
