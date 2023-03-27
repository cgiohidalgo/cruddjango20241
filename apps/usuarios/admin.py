from django.contrib import admin

# Register your models here.

from .models import Cliente, AdministradorDuenio, Carrito

admin.site.register(Cliente)
admin.site.register(AdministradorDuenio)
admin.site.register(Carrito)