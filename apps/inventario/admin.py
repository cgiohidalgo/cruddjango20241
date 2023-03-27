from django.contrib import admin
from .models import Categoria, SubCategoria, Producto, DetallesProducto, Bodega, Proveedor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto)
admin.site.register(DetallesProducto)
admin.site.register(Proveedor)
admin.site.register(Bodega)
