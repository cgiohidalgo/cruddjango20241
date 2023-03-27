from django.urls import include, path

from ventas.views import *

app_name='ventas'
urlpatterns = [

    path('descuentos', descuentos, name='descuentos'),

    path('descuentoCrear', crearDescuento, name='descuentoCrear'),
    path('descuentoCrear/<int:idCategoria>', crearDescuentoCategoria, name='descuentoCrearCategoria'),
    path('descuentoCrear/<int:idCategoria>/<int:idSubCategoria>', crearDescuentoSubCategoria, name='descuentoCrearSubCategoria'),
    path('descuentoCrear/<int:idCategoria>/<int:idSubCategoria>/<int:idProducto>', crearDescuentoProducto, name='descuentoCrearProducto'),

    path('descuentoModificar', modificarDescuento, name='descuentoModificar'),
    
    #path('descuentoModificar/<int:idCategoria>', modificarDescuentoCategoria, name='descuentoModificarCategoria'),
    #path('descuentoModificar/<int:idCategoria>/<int:idSubCategoria>', modificarDescuentoSubCategoria, name='descuentoModificarSubCategoria'),
    #path('descuentoModificar/<int:idCategoria>/<int:idSubCategoria>/<int:idProducto>', modificarDescuentoProducto, name='descuentoModificarProducto'),

    path('descuentoCrud', descuentoCrud, name='descuentoCrud'),
    path('descuentoConsultar', descuentoConsultar, name='descuentoConsultar'),
]