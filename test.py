from django.test import TestCase
from inventario.models import *
from usuarios.models import *

#FUNCIÓN - PRIMERA PRUEBA
def bodegaconsulta(idBodega):
    categorias = Categoria.objects.all() #para cargar las categorias en el navbar
    bodegas = Bodega.objects.all()

    #modificar = request.POST

    if(idBodega=='-1' or idBodega==None):
        ciudadBodega = ""
        dirBodega = ""        
    else:
        BodegaObject = Bodega.objects.get(pkBodega=idBodega)
        ciudadBodega = BodegaObject.ciudad
        dirBodega = BodegaObject.direccion

    return {'idBodega':idBodega,'ciudadBodega':ciudadBodega,'dirBodega':dirBodega}


#FUNCIÓN - SEGUNDA PRUEBA
def duenioAdminIngreso(request, ingresar):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    #ingresar = request.POST
    if(request.get('method') == 'POST'):
        admin = AdministradorDuenio(            
            nombreUsuario=ingresar.get('nombreUsuario'),
            clave=ingresar.get('clave'),
            tipo='ADMIN'
        )

        duenio=AdministradorDuenio(
            nombreUsuario=ingresar.get('nombreUsuario'),
            clave=ingresar.get('clave'),
            tipo='CEO'
        )
        nombre=ingresar.get('nombreDuenioAdmin')
        if (admin.autenticarAdmin()):
            #messages.success(request, f'¡Bienvenido {nombre}!')
            return "ADMIN"
        elif (duenio.autenticarDuenio()):            
            #messages.success(request, f'¡Bienvenido {nombre}!')
            return "DUENIO"
        else:
            #messages.info(request, 'Cuenta de usuario o contraseña invalida')
            return "INVALIDO"
    return "SEND"


#FUNCION - CUARTA PRUEBA
def consultarReferencias(categoria, subcategoria, producto):
    categorias = Categoria.objects.all()
    idcategoria = categoria
    subcategorias = {}
    idsubcategoria = subcategoria
    productos = {}
    idproducto = producto
    catSeleccionada = False
    subCatSeleccionada = False
    producSeleccionado = False
    
    if((categoria != "") and (categoria != None) and (categoria != "-1")):
        subcategorias = SubCategoria.objects.filter(fkCategoria=idcategoria)
        catSeleccionada = True
    else:
        idcategoria = -1
    if((subcategoria != "") and (subcategoria != None) and (subcategoria != "-1")):
        productos = Producto.objects.filter(fkSubCategoria=idsubcategoria)
        subCatSeleccionada = True
    else:
        idsubcategoria = -1
    if((producto != "") and (producto != None) and (producto != "-1")):                
        idproducto = producto
        producSeleccionado = True
    else:
        idproducto = -1

    context={
        'nombre': "",
        'descripcion': "",
        'iva': "",
        'precio': "",
        'rutaImagen': "",
    }

    if((idproducto != "") and (idproducto != None) and (idproducto != "-1") and (idproducto != -1)): #SE CARGAN LOS VALORES DE LA REFERENCIA
        producObject = Producto.objects.get(pkProducto=idproducto)
        nombreO = producObject.nombre
        descripcionO = producObject.descripcion        
        precioO = producObject.precio
        ivaO = producObject.iva
        rutaImagenO = producObject.rutaImagen

        context={
            'nombre': nombreO,
            'descripcion': descripcionO,
            'iva': int(ivaO),
            'precio': precioO,
            'rutaImagen': "../"+rutaImagenO.name,
        }

    return context

#PRUEBAS
class PruebasFunciones(TestCase):

    def setUp(self):
        print("preparando contexto")
        #CONTEXTO FUNC 1
        self.bodega1 = Bodega(pkBodega=1,
                              direccion="1",
                              ciudad = "11").save()
        self.bodega1Datos = {'idBodega':1,'dirBodega':"1",'ciudadBodega':"11"}#if idBodega==1

        self.bodega2 = Bodega(pkBodega=2,
                              direccion="2",
                              ciudad = "22").save()
        self.bodega2Datos = {'idBodega':2,'dirBodega':"2",'ciudadBodega':"22"} #if idBodega==2

        self.bodega3Datos = {'idBodega':"-1",'dirBodega':"",'ciudadBodega':""} #if idBodega=="-1"
        self.bodega4Datos = {'idBodega':None,'dirBodega':"",'ciudadBodega':""} #if idBodega == None

        #CONTEXTO FUNC 2
        self.request1 = {'method':"POST"}#TRUE
        self.request2 = {'method':"SEND"}#FALSE

        self.duenio = AdministradorDuenio(pkAdministradorDuenio = 1,
                                          nombreUsuario="Duenio",
                                          clave="123",
                                          tipo="CEO").save()
        self.duenioDatos = {'nombreUsuario':"Duenio", 'clave':"123",'tipo':"CEO"}        

        self.admin = AdministradorDuenio(pkAdministradorDuenio = 2,
                                         nombreUsuario="Admin",
                                         clave="123",
                                         tipo="ADMIN").save()
        self.adminDatos = {'nombreUsuario':"Admin", 'clave':"123",'tipo':"ADMIN"}

        self.noUser = {'nombreUsuario':"user", 'clave':"0",'tipo':"Nada"}

        
        self.categoria = Categoria(nombreCategoria="Hombres",rutaImagen= "../media/categoriasImagenes/categorias.jpg").save()
        self.subCategoria = SubCategoria(fkCategoria=Categoria.objects.get(nombreCategoria="Hombres"),nombreSubCategoria= "CamisetasM").save() 
        self.producto = Producto(   fkSubCategoria= SubCategoria.objects.get(nombreSubCategoria="CamisetasM"),
                                    nombre= "Camiseta1",
                                    descripcion= "descripcion1",
                                    iva= 19.0,
                                    precio= 23000,
                                    rutaImagen= "../media/productosImagenes/Camiseta1.jpg").save()

        self.productoDatos = {'nombre': "Camiseta1",
                                'descripcion': "descripcion1",
                                'iva': 19.0,
                                'precio': 23000,
                                'rutaImagen': "../media/productosImagenes/Camiseta1.jpg"}
        
        self.producto2 = Producto(   fkSubCategoria= SubCategoria.objects.get(nombreSubCategoria="CamisetasM"),
                                    nombre= "Camiseta2",
                                    descripcion= "descripcion2",
                                    iva= 19.0,
                                    precio= 23000,
                                    rutaImagen= "../media/productosImagenes/Camiseta1.jpg").save()

        self.productoDatos2 = {'nombre': "Camiseta2",
                                'descripcion': "descripcion2",
                                'iva': 19.0,
                                'precio': 23000,
                                'rutaImagen': "../media/productosImagenes/Camiseta2.jpg"}


    
    def test_consultarReferencias(self):
        print("Realizando la prueba consultarReferencias)
        self.assertEqual(consultarReferencias(1,3,0),self.productoDatos)
        self.assertEqual(consultarReferencias(1,'-1','-1'),self.productoDatos2)


    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.bodega1)
        del(self.bodega2)
        del(self.bodega1Datos)
        del(self.bodega2Datos)
        del(self.request1)
        del(self.request2)
        del(self.duenio)
        del(self.duenioDatos)
        del(self.admin)
        del(self.adminDatos)
        del(self.noUser)
        del(self.producto)
        del(self.productoDatos)
        del(self.producto2)
        del(self.productoDatos2)