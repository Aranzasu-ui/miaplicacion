from django.shortcuts import render

# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Instanciamos el modelo 'Postres' para poder usarlo en nuestras Vistas CRUD
from .models import Postres

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse
 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages 
 
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin 
 
# Habilitamos los formularios en Django
from django import forms

class PostresListado(ListView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    template_name = 'postres/index.html'
class PostreCrear(SuccessMessageMixin, CreateView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
    template_name = 'postres/crear.html'

 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class PostreDetalle(DetailView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    templates_name = 'postres/detalles.html'
class PostreActualizar(SuccessMessageMixin, UpdateView): 
    model = Postres # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Postres # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
    template_name = 'postres/actualizar.html'
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class PostreEliminar(SuccessMessageMixin, DeleteView): 
    model = Postres 
    form = Postres
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'