from django.urls import include, path
from usuarios.views import *
from django.contrib.auth import views as auth_views

app_name='usuarios'

urlpatterns = [
    #path('principalAdmin/<int:id_dueno>/',paginaPrincipal_admin,name='paginaPrincipal_admin'),
    path('principalAdmin',paginaPrincipal_admin,name='paginaPrincipal_admin'),
    path('duenioAdminIngreso/', duenioAdminIngreso, name='duenioAdminIngreso'),
    path('principalDuenio/', paginaPrincipal_duenio, name='paginaPrincipal_duenio'),
    path('adminMenu/', adminMenu, name='duenioAdminMenu'),
    path('clienteMenu/', clienteMenu, name='duenioClienteMenu'),
    path('duenioAdminAgregar/', duenioAdminAgregar, name='duenioAgregarAdmin'),
    path('clienteingresar', clienteIngreso, name='ingreso'),
    path('clienteregistro',clienteregistro, name='registro'),
    path('clientecerrarsesion', clienteCerrarSesion, name='cerrarsesion'),
    path('duenioAdminModificar/', duenioAdminModificar, name='duenioModificarAdmin'),
    path('duenioClienteConsultar/', duenioClienteConsultar, name='duenioClienteConsultar'),
    path('duenioAdminConsultar/', duenioAdminConsultar, name='duenioAdminConsultar'),
    path('clienteinicio/<str:nombre>', clienteInicio, name='inicioCliente'),
    path('clientePerfil/<str:nombre>/', clientePerfil, name='clientePerfil'),
    path('clienteHistorialCompras/<str:nombre>/', clienteHistorialCompras, name='clienteHistorialCompras'),
    path('duenioAdminEliminar/', duenioAdminEliminar, name='duenioEliminarAdmin'),
    path('clienteEliminar/<str:nombre>/', clienteEliminar, name='clienteEliminar'),
    path('carrito/<str:nombre>/', clienteCarrito, name='clienteCarrito'),

]
