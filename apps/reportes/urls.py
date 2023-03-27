from django.urls import include, path
from reportes.views import *

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'reportes'
urlpatterns = [
    path('inicioReportes', inicioReportes, name='inicioReportes'),
    path('reporteVentas', reporteVentas, name='reporteVentas'),
    path('reporteProducto', reporteProducto, name='reporteProducto'),
    path('reporteVentasCategoria', reporteVentasCategoria, name='reporteVentasCategoria'),
    path('reporteTopClientes', reporteTopClientes, name='reporteTopClientes'),
    path('reportePocasUnidades', reportePocasUnidades, name='reportePocasUnidades'),
    path('masVendidos/', masVendidos, name='masVendidos'),
    path('menosVendidos/', menosVendidos, name='menosVendidos'),
    path('reporteCumpleañosCliente', reporteCumpleañosCliente, name='reporteCumpleañosCliente'), 
    path('reporteProductosCliente', reporteProductosCliente, name='reporteProductosCliente')
]
