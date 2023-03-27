
# Nova 

[![postgreSQL version](https://img.shields.io/badge/Django-v2.0_v3.0-purple.svg?style=flat-square)](https://www.postgresql.org/)

## Proyecto Desarrollo II 

Para la primera instalación:

```
docker-compose build
docker-compose up
```

Admin default para tablas por localhost:8000/admin
```
admin
123
```

Tenemos usuarios default ejemplos:

```
duenio:     'Marthox', '1234'

admins:     'Valeria', '1234'
            'Emily', '1234'

clientes:   'Felipe', '1234'
            'Jaime', '1234'
```

## Si no esta funcionando el entrypoint

y como es la primera vez hay que migrar la prueba de modelo

```
docker exec -it nombre_del_docker_django python manage.py makemigrations
docker exec -it nombre_del_docker_django python manage.py migrate
```

nota: ultima columna es el nombre del docker (debe ser algo como con web)

```
docker ps -a
```