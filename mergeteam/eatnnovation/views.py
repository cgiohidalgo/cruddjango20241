from django.shortcuts import render

# Create your views here.
 
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
# Instanciamos el modelo 'Arepa' para poder usarlo en nuestras Vistas CRUD
from .models import Arepa


# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms


class ArepaListado(ListView):
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 

class ArepaCrear(SuccessMessageMixin, CreateView):
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Creada Correctamente!' # Mostramos este Mensaje luego de Crear un Postre
        
# Redireccionamos a la página principal luego de crear un registro o arepa    
    def get_success_url(self):
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ArepaDetalle(DetailView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 


class ArepaActualizar(SuccessMessageMixin, UpdateView): 
    model = Arepa # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Arepa # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Arepa Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 
    
    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ArepaEliminar(SuccessMessageMixin, DeleteView): 
    model = Arepa 
    form = Arepa
    fields = "__all__"     
    
        # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Arepa Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'