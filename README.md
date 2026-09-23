# Welcome to DotAxion Visión Arquitectónica ERP Project! 

Backend ERP, construida con FastAPI.

## Setup local con Dev Containers

1. Instala Docker Desktop y la extensión **Dev Containers** de VS Code.
2. Abre este repositorio en VS Code y ejecuta `Dev Containers: Reopen in Container` desde la paleta de comandos.
3. Espera a que termine la construcción: el contenedor instala las dependencias de producción y desarrollo automáticamente.

El contenedor reenvía el puerto `8000` al equipo local.

## Ejecutar la API

Dentro del Dev Container, ejecuta:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en `http://localhost:8000` y la documentación interactiva en `http://localhost:8000/docs`.

## Arquitectura

El proyecto sigue una arquitectura hexagonal:

- `app/domain`: reglas de negocio, modelos, casos de uso y puertos (contratos).
- `app/adapters`: implementaciones de los puertos.
- `app/workflows`: orquestación de cada operación de la aplicación y sus modelos de entrada/salida.
- `app/routes`: adaptadores HTTP de FastAPI que reciben solicitudes y delegan en los workflows.
- `app/dependencies.py`: composición de dependencias para conectar rutas, puertos y adaptadores concretos.

Así, el dominio no depende de FastAPI ni del almacenamiento concreto, lo que facilita cambiar adaptadores sin alterar las reglas de negocio.
