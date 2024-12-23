# **Football Microservices**

## **Descripción**

Este proyecto implementa una arquitectura de microservicios utilizando **FastAPI** y **MongoDB**. Contiene tres servicios:

- **Player-Service**: Gestiona información de jugadores.
- **Team-Service**: Gestiona equipos.
- **Stats-Service**: Gestiona estadísticas de partidos.

Los servicios están orquestados mediante **Docker Compose** y MongoDB se usa como base de datos.

## **Tecnologías**

- **FastAPI**: Framework para construir APIs RESTful.
- **MongoDB**: Base de datos NoSQL.
- **Docker**: Para contenerizar los servicios.
- **Docker Compose**: Orquestación de servicios.

## **Requisitos Previos**

1. **Docker** y **Docker Compose** instalados. Si no los tienes, sigue la [guía oficial](https://docs.docker.com/get-docker/).

## **Instrucciones de Ejecución**

### 1. Clonar el Repositorio

```bash
git clone https://github.com/EdissonF-UNSA/AppFutbol-microservicios.git
cd football-microservices
```

### 2. Levantar los Servicios

Ejecuta el siguiente comando para construir y levantar los contenedores:

```bash
docker-compose up --build
```

Esto iniciará:

- **Player Service** en [http://127.0.0.1:8001](http://127.0.0.1:8001)
- **Team Service** en [http://127.0.0.1:8002](http://127.0.0.1:8002)
- **Stats Service** en [http://127.0.0.1:8003](http://127.0.0.1:8003)
- **MongoDB** en [http://127.0.0.1:27018](http://127.0.0.1:27018)

### 3. Detener los Servicios

Cuando termines, puedes detener los servicios con:

```bash
docker-compose down
```

## **Interacción con los Servicios**

- **Navegador**: Accede a las URLs mencionadas arriba para ver los datos de los servicios.
- **Postman**: Utiliza Postman para realizar peticiones POST y GET a los endpoints.
