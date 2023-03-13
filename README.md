# Proyecto LS3 - 2023 - 1


# Instalar python 3

- sudo apt-get update
- sudo apt-get install python3.6

### Instalar el ambiente virtual (esto es opcional, solo si no se quiere usar toda la maquina, sino solo ambiente virtual)

- pip3 install virtualenv
- python3 -m venv nombre_ambiente
- source nombre_ambiente/bin/activate  #ingresar al ambiente

# Django 
### Instalar dajngo  

- pip3 install django

### Crear un nuevo proyecto en Django

- django-admin startproject nombre_proyecto

### Crear una aplicación (app) en Django

- python manage.py startapp nombre_app
    - Registrar una app en el proyecto:
        -  En settings.py, este archivo se encuentra en nombre_proyecto > nombre_proyecto > settings.py 
        -  Abro el archivo settings.py y voy a la sección que dice INSTALLED_APPS y registro la app. Al pongo ('nombre_app',) 

# Instalar Docker y Docker compose (Linux & Mac)
### Instalar docker (esto se debe hacer por fuera del ambiente)
- sudo apt update
- sudo apt install apt-transport-https ca-certificates curl software-properties-common
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add –
- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
- sudo apt update
- apt-cache policy docker-ce
- sudo apt install docker-ce

### Instalar docker compose
- sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
- sudo chmod +x /usr/local/bin/docker-compose

### Instalar el motor de bases de datos PostgreSQL usando Docker (para mas detalles ver el archivo)
- docker-compose up -d

## Crear el modelo de datos  en models.py (el archivo que se encuentra en el directorio nombre_app)
- estrcutura: una clase para definir el nombre de la tabla y su atributos
    class Users(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    precio = models.CharField(max_length=20, default='DEFAULT VALUE')
    stock = models.CharField(max_length=100, default='DEFAULT VALUE')
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'users' # Le doy un nombre a la  tabla en la Base de Datos

## Migrar los datos de models.py a la base de datos 
- python manage.py makemigrations nombre_app

## crear la tabla en la base de datos de Postgres
- python manage.py migrate
 
## Hacer la conexión de la base de datos con Django
- Intalar el conector, usando "pip3 install psycopg2-binary==2.9.5"



by GHS