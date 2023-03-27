from django.urls import include, path
from inventario.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'inventario'
urlpatterns = [
    path('bodegainicio', bodegaInicio, name='bodegainicio'),
    path('bodegaregistro', bodegaRegistro, name='bodegaregistro'),    
    path('bodegaconsulta', bodegaconsulta, name='bodegaconsulta'),
    path('bodegaModificar', modificarBodega , name='bodegaModificar'),
    path('bodegaEliminar', bodegaEliminar, name='bodegaEliminar'),
    path('eliminarcategorias', eliminarCategorias, name='eliminarCategorias'),
    path('consultarcategorias', consultarcategorias, name='consultarcategorias'),
    path('modificarCategoria',modificar_categoria,name='modificar_categoria'),
    path('categoria', categoria, name='categoria'),
    path('categoriaCrear', aniadirCategoria, name='aniadirCategoria'),
    path('categoriaModificar', modificar_categoria, name='modificar_categoria'),
    path('productos', productos, name='productos'),
    path('productosCrearPrincipal', productosCrearPrincipal, name='productosCrearPrincipal'),
    path('productosCrear', aniadirProductos, name='aniadirProductos'),
    path('referenciasCrear', aniadirReferencias, name='aniadirReferencias'),
    path('productosModificarPrincipal', productosModificarPrincipal, name='productosModificarPrincipal'),
    path('productosModificar', modificarProductos, name='modificarProductos'),
    path('referenciasModificar', modificarReferencias, name='modificarReferencias'),
    path('productosConsultarPrincipal', productosConsultarPrincipal, name='productosConsultarPrincipal'),
    path('productosConsultar', consultarProductos, name='productosConsultar'),
    path('referenciasConsultar', consultarReferencias, name='referenciasConsultar'),
    path('productosEliminarPrincipal', productosEliminarPrincipal, name='productosEliminarPrincipal'),
    path('productosEliminar', eliminarProductos, name='eliminarProductos'),
    path('referenciasEliminar', eliminarReferencias, name='eliminarReferencias'),
    path('proveedor', proveedor, name='proveedor'),
    path('proveedorCrear', aniadirProveedor, name='aniadirProveedor'),

    path('proveedorModificar', modificarProveedor, name='modificarProveedor'),
    path('proveedorEliminar', eliminarProveedor, name='eliminarProveedor'),
    path('productosCategorias/<str:nombre>/<str:categoria>/', productosCategoriasVista, name='productosCategorias'),
    path('productosCategorias/<str:nombre>/<str:categoria>/<str:subCategoria>/', productosSubCategoriasVista, name='productosSubCategorias'),
    path('productoDetalles/<str:nombre>/<str:categoria>/<str:idproducto>/<str:precio>',productoDetalles,name='productoDetalles'),    
]

