# Proyecto LS3 - 2023 - 1

El modelo para el desarrollo de este CRUD, se toma del equipo MergeTeam, del curso LSIII 2023-1

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

## Hacer la conexión de la base de datos con Django
- Intalar el conector, usando:\
pip3 install psycopg2-binary==2.9.5

## configurar la base de datos 
- En el settings.py/

{% filename %}

    DATABASES = {
        'default': {
            'ENGINE' : 'django.db.backends.postgresql_psycopg2',
            'NAME' : 'productos',
            'USER' : 'root',
            'PASSWORD' : 'root',
            'HOST' : 'localhost',
            'PORT' : '5432', #si lo dejas vacío tomara el puerto por default
        }
    }

## Crear el modelo de datos  en models.py (el archivo que se encuentra en el directorio nombre_app)
- estructura: una clase para definir el nombre de la tabla y su atributos

{% filename %}

    class Arepa(models.Model):  #nombre de la tabla en la Base de Datos
        nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
        precio = models.CharField(max_length=20, default='DEFAULT VALUE')
        #stock = models.TextChoices('Si Hay', 'No hay')
        stock = models.CharField(max_length=100, default='DEFAULT VALUE')
        img = models.FileField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'arepas' #nombre de instancia con la que llamamos la tabla en la Base de Datos

## Migrar los datos de models.py a la base de datos 
- python manage.py makemigrations nombre_app

## crear la tabla en la base de datos de Postgres
- python manage.py migrate

# Vistas Genéricas

El Framework Django trabaja sobre la arquitectura MTV que son las iniciales de Model Template View que traducido al español significa Modelo Plantilla Vista.

Cuando creamos este proyecto, Django nos generó un archivo llamado views.py (dentro de nombre_app) donde podemos definir las vistas y otras tareas para nuestro proyecto. Estas vistas genéricas nos permiten realizar de manera facil un CRUD son Create, Read, Update y Delete, que en vistas genéricas son:

- ListView
- DetailView
- CreateView
- UpdateView
- DeleteView

## Instanciar las vistas genéricas de Django y mi modelo

- Abrimos nombre_app -> views.py

## Instanciar 3 utilidades necesarias para este proyecto, estas son reverse, messages y forms.

#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
#Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
#Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
#Habilitamos los formularios en Django\
from django import forms


## Creare unas clases para poder usar las vistas genéricas de Django: ListView, DetailView, CreateView, UpdateView y DeleteView.

#Listado de Registros o Arepas

{% filename %}

    class ArepasListado(ListView):
        model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 

## Crear (Create)

Creo una clase con el nombre ArepaCrear que usará la vista genérica CreateView en donde mostraremos un formulario para crear un nuevo registro o arepa

{% filename %}

    class ArepaCrear(SuccessMessageMixin, CreateView): 
        model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
        form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
        fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
        success_message = 'Arepa Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa
    
        # Redireccionamos a la página principal luego de crear un registro o arepa
        def get_success_url(self):        
            return reverse('leer') # Redireccionamos a la vista principal 'leer'

## Leer (Read)

Creo una clase con el nombre ArepaDetalle que usará la vista genérica DetailView la cual se encargará de mostrar los detalles de una arepa o registro:

{% filename %}

    class ArepaDetalle(DetailView): 
        model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 

## Actualizar (Update)
Creo una clase con el nombre ArepaActualizar que usará la vista genérica UpdateView, en esta vista mostraremos un formulario para actualizar una arepa o registro:

{% filename %}

    class ArepaActualizar(SuccessMessageMixin, UpdateView): 
        model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
        form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
        fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
        success_message = 'Arepa Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 
    
        # Redireccionamos a la página principal luego de actualizar un registro o arepa
        def get_success_url(self):               
            return reverse('leer') # Redireccionamos a la vista principal 'leer'
 
## Eliminar (Delete)
Por último creo una clase con el nombre ArepaEliminar que hara uso de la vista genérica DeleteView, esta vista la usaremos para eliminar un registro o arepa de nuestra base de datos

{% filename %}

    class ArepaEliminar(SuccessMessageMixin, DeleteView): 
        model = Arepa 
        form = Arepa
        fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o arepa
        def get_success_url(self): 
            success_message = 'Arepa Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
            messages.success (self.request, (success_message))       
            return reverse('leer') # Redireccionamos a la vista principal 'leer'

# Rutas (urls)

## Instanciar las vistas genéricas de Django y mi modelo

- Abrimos nombre_app -> views.py

Dentro del archivo urls.py agrego las siguientes rutas dentro de urlpatterns = [], mediante estas rutas llamamos a una determinada vista HTML, estas vistas HTML las crearé más adelante.

{% filename %}

    from django.contrib import admin
    from django.urls import path 
    from  nombre_app.views import ArepaListado, ArepaDetalle, ArepaCrear, ArepaActualizar, ArepaEliminar


    urlpatterns = [

        path('admin/', admin.site.urls),

        # La ruta 'leer' en donde listamos todos los registros o arepas de la Base de Datos
        path('arepas/', ArepaListado.as_view(template_name = "arepas/index.html"), name='leer'),
    
        # La ruta 'detalles' en donde mostraremos una página con los detalles de un arepas o registro 
        path('arepas/detalle/<int:pk>', ArepaDetalle.as_view(template_name = "arepas/detalles.html"), name='detalles'),
    
        # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo arepas o registro  
        path('arepas/crear', ArepaCrear.as_view(template_name = "arepas/crear.html"), name='crear'),
    
        # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un arepas o registro de la Base de Datos 
        path('arepas/editar/<int:pk>', ArepaActualizar.as_view(template_name = "arepas/actualizar.html"), name='actualizar'), 
    
        # La ruta 'eliminar' que usaremos para eliminar un arepas o registro de la Base de Datos 
        path('arepas/eliminar/<int:pk>', ArepaEliminar.as_view(), name='eliminar'),   
    ]

- Mediante las rutas que definí en el código anterior, estoy llamando a las vistas genéricas (clases) que definimos en la seección "Vistas Genéricas", por ejemplo en la ruta arepas/crear llamamos a la clase ArepaCrear la cual debe llamar al template o vista crear.html que se encuentra dentro de la carpeta arepas y al final le asignamos un nombre a esta ruta, el nombre que le asignamos es crear.

- Siempre debemos pasarle a estas 3 rutas el id del registro o arepa con <int:pk> en donde int es integer y pk es primary key, ya que de esta manera Django puede saber cual es el registro que debe de leer, actualizar y eliminar de la Base de Datos.


# Vistas HTML con Bootstrap 4

En la vista principal voy a mostrar una tabla HTML en donde se listarán los registros o arepas desde la base de datos, colocaré una tabla HTML de Bootstrap 4 con las columnas Nombre, Precio, Stock, Imagen y Acciones.

En esta  sección creamos 4 archivos HTML dentro de nuestra carpeta templates que son actualizar.html, crear.html, detalles.html e index.html

Dentro el archivo urls.py que configuré anteriormente, podemos ver que cada ruta está llamando a un archivo HTML con la vista correspondiente que debe de mostrar dicha ruta, tenemos que crear un directorio llamado templates en donde crearemos 4 archivos HTML que son actualizar.html, crear.html, detalles.html y index.html

## Instalación y Configuración de Paquetes

### Bootstrap 4

El Framework Bootstrap 4 nos permite crear interfaces HTML de manera rápida, asi nos enfocamos solamente en la lógica de la aplicación. Voy a instalar la librería django-bootstrap4 ejecutando el siguiente comando, esta librería nos instala Bootstrap 4 dentro del Framework Django (info: https://pypi.org/project/django-bootstrap4/):

- pip install django-bootstrap4

### Django Widget Tweaks

Ahora instalaré el paquete django-widget-tweaks que me permite renderizar y gestionar los campos de los formularios de manera ágil, ejecuto el siguiente comando para instalarlo:

- pip install django-widget-tweaks 

### Agregar al settings Bootstrap 4 y Widget Tweaks

-  Abro el archivo settings.py y voy a la sección que dice INSTALLED_APPS y registro los paquetes. Al pongo ('bootstrap4','widget_tweaks',) 

### Creación de URL 

En el archivo settings.py: 

    #La URL para los archivos Estáticos (CSS, JS, Imágenes, etc.)
    STATIC_URL = '/static/' 
    
    #Las rutas para las imágenes de cada registro o arepas 
    MEDIA_URL = '/arepas/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'arepas/static/uploads')

### Creación de html

- En nombre_app -> creamos la carpeta "templates" 
    - creamos la carpeta "arepas" 
        - creamos actualizar.html, crear.html, detalles.html, index.html   
       

## Crear el index.html 

Aqui se muestra la columna Acciones colocaré 3 botones que son Ver, Editar y Eliminar para cada registro o Arepa.

Puedes ver en el código del archivo crear.html que estamos usando la librería widget_tweaks que instalamos previamente, esta librería nos permite gestionar nuestros formularios creados mediante Vistas Genéricas de Django.

{% filename %}

   <form method="post" enctype="multipart/form-data">
    
        <!-- Pasamos el 'csrf_token' de seguridad para poder crear un nuevo registro -->
        {% csrf_token %}
        
        <!-- {{ form.as_p }} -->
        <div class="form-group">
            <label for="nombre" class="txt_negrita">Nombre</label>
            {{ form.nombre|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
        </div>
        <div class="form-group">
            <label for="precio" class="txt_negrita">Precio</label>
            {{ form.precio|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto --> 
        </div>
        <div class="form-group">
            <label for="stock" class="txt_negrita">Stock</label>
            {{ form.stock|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
        </div>
        <div class="form-group">
            <label for="img" class="txt_negrita">Imagen</label>
            {{ form.img|add_class:"form-control mb-3" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
        </div>
        
        <button type="submit" class="btn btn-primary">Aceptar</button>
        <a href="./" type="submit" class="btn btn-primary">Cancelar</a>
        
    </form>

## Crear el deatlles.html 

Dentro de esta vista vamos a mostrar los detalles de un archivo independientemente cada ves que el usuario haga clic en el botón Ver que se encuentra en la columna Acciones.

{% filename %}

    <h4>Detalles</h4>
    
        <p><span class="txt_negrita">Nombre:</span> <br> {{object.nombre}}</p>
        <p><span class="txt_negrita">Precio:</span> <br> {{object.precio}}</p>
        <p><span class="txt_negrita">Stock:</span> <br> {{object.stock}}</p>
        <p><span class="txt_negrita">Imagen:</span> <br> <img src="{% static 'uploads/'%}{{object.img}}" alt="{{object.nombre}}" class="img-fluid"> </p>
        <p><span class="txt_negrita">Creado:</span> <br> {{object.created_at}}</p>
        <p><span class="txt_negrita">Actualizado:</span> <br> {{object.updated_at}}</p>
    
        <!-- Botón para volver a la vista principal (Home) -->
        <a href="../" type="submit" class="btn btn-primary">Volver</a>


## Crear  actualizar.html

{% filename %}

    <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            
            <!-- {{ form.as_p }} -->
            <div class="form-group">
            <label for="nombre" class="txt_negrita">Nombre</label>
            {{ form.nombre|add_class:"form-control" }} <!-- Usamos la librería 'widget_tweaks' para crear esta caja de texto -->
            </div>
            <div class="form-group">
            <label for="precio" class="txt_negrita">Precio</label>
            {{ form.precio|add_class:"form-control" }}
            </div>
            <div class="form-group">
            <label for="stock" class="txt_negrita">Stock</label>
            {{ form.stock|add_class:"form-control" }}
            </div>
            <div class="form-group">
            <label for="img" class="txt_negrita">Imagen</label>
            {{ form.img|add_class:"form-control mb-3" }}
            <p class="txt_negrita">Imagen Actual:</p>
            <img src="{% static 'uploads/'%}{{object.img}}" class="img-fluid" alt="{{object.nombre}}">
            </div>
        
            <button type="submit" class="btn btn-primary">Aceptar</button>
            <a href="../" type="submit" class="btn btn-primary">Volver</a>
        
        </form> 

by GHS
