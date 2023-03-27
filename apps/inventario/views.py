from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_protect
from inventario.models import *
from ventas.models import *
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import math
from django.core.files import File
import os 


def bodegaInicio(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request,'inventario/bodegainicio.html', context,{})

@csrf_protect
def bodegaRegistro(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    crearBodega = request.POST
    if(request.method == 'POST'):
        bodega = Bodega(
            direccion = crearBodega.get('direccion'),
            ciudad = crearBodega.get('ciudad')
        )
        try:
            bodega.full_clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no es(son) validos')
            return render(request,'inventario/bodegaregistro.html', context,{'form':crearBodega})
        bodega.save()
        messages.success(request, 'La bodega ha sido creada correctamente')
        return redirect(to='inventario:bodegaregistro')
    return render(request, 'inventario/bodegaregistro.html', context,{'form':crearBodega})

def bodegaconsulta(request, *args, **kwargs):
    categorias = Categoria.objects.all() #para cargar las categorias en el navbar
    bodegas = Bodega.objects.all()

    modificar = request.POST
    idBodega = modificar.get('bodega')

    if(idBodega=='-1' or idBodega==None):
        ciudadBodega = ""
        dirBodega = ""
    else:
        BodegaObject = Bodega.objects.get(pkBodega=idBodega)
        ciudadBodega = BodegaObject.ciudad
        dirBodega = BodegaObject.direccion


    context={'categorias':categorias, 'bodegas':bodegas, 'ciudadBodega':ciudadBodega, 'dirBodega':dirBodega}    
    return render(request, 'inventario/bodegaconsulta.html', context, {})

def bodegaEliminar(request, *args, **kwargs):
    bodegas = Bodega.objects.all()

    modificar = request.POST
    idBodega = "-1"
    ciudadBodega = ""
    dirBodega = ""
    

    if(request.method=="POST"):
        idBodega = modificar.get('bodega')
        if(idBodega!='-1' or idBodega!=None):
            BodegaObject = Bodega.objects.get(pkBodega=idBodega)
            ciudadBodega = BodegaObject.ciudad
            dirBodega = BodegaObject.direccion

            detallesP = DetallesProducto.objects.filter(fkBodega=idBodega)

            if((len(detallesP) > 0) and (detallesP != None)):
                messages.info(request, 'Esta referencia tiene productos asociados ¿Está seguro que desea eliminarla?')

            if (modificar.get('bodega-submit')=="Eliminar Bodega"): #Se Elimina La Bodega            
                try:
                    Bodega.objects.get(pkBodega=idBodega).delete()
                except ValidationError as e:
                    messages.info(request, 'Bodega no registrada en el sistema')
                
                #print("HOLAAAAAAAAAA")
                context={'bodegas':bodegas, 'ciudadBodega':'', 'dirBodega':'', 'idBodega':-1}
                return render(request, 'inventario/bodegaEliminar.html', context, {})

    context={'bodegas':bodegas, 'ciudadBodega':ciudadBodega, 'dirBodega':dirBodega, 'idBodega':int(idBodega)}    
    return render(request, 'inventario/bodegaEliminar.html', context, {})

def consultarcategorias(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    nombreO = ""
    rutaImagenO = ""
    idcategoria = "-1"
    context={'categorias':categorias, 'nombreO':nombreO, 'rutaImagenO':rutaImagenO, 'idcategoria':idcategoria}

    datos = request.POST
    if(request.method=="POST"):
        idcategoria = datos.get('categoria')
        if(idcategoria!="-1" and idcategoria != None):
            idcategoria = datos.get('categoria')
            categoria = Categoria.objects.get(pkCategoria=idcategoria)
            nombreO = categoria.nombreCategoria
            rutaImagenO = categoria.rutaImagen
            
            context={'categorias':categorias,
                     'nombreO':nombreO,
                     'rutaImagenO': "../"+rutaImagenO.name,
                     'idcategoria':int(idcategoria)}
    
    return render(request,'inventario/categoriasconsultar.html', context,{})

def eliminarCategorias(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    nombreO = ""
    rutaImagenO = ""
    idcategoria = "-1"
    context={'categorias':categorias, 'nombreO':nombreO, 'rutaImagenO':rutaImagenO, 'idcategoria':idcategoria}

    datos = request.POST
    if(request.method=="POST"):
        idcategoria = datos.get('categoria')
        if(idcategoria!="-1" and idcategoria != None):
            if(datos.get('categoria-submit')=="Eliminar Categoria"):
                try:
                    Categoria.objects.filter(pkCategoria=idcategoria).delete()
                    messages.success(request, 'Categoria eliminada exitosamente')
                    return render(request,'inventario/categoriasEliminar.html', context,{})
                except:
                    messages.warning(request, 'Esta categoria ya ha sido eliminada')
                    return render(request,'inventario/categoriasEliminar.html', context,{})

            #SE CARGAN LOS CAMPOS
            else:
                #idcategoria = datos.get('categoria')
                categoria = Categoria.objects.get(pkCategoria=idcategoria)
                nombreO = categoria.nombreCategoria
                rutaImagenO = categoria.rutaImagen

                subcat = SubCategoria.objects.filter(fkCategoria=idcategoria)
                if((len(subcat) > 0) and (subcat != None)):
                    messages.info(request, 'Esta Categoria tiene subCategorias asociadas ¿Está seguro que desea eliminarla?')
                    hayReferencias = False
                    referencias = []

                    for subcate in subcat:
                        refers = Producto.objects.filter(fkSubCategoria=subcate.pkSubCategoria)

                        if((len(refers) > 0) and (refers != None)):
                            hayReferencias = True

                            for rf in refers:
                                referencias.append(rf.pkProducto)

                    if(hayReferencias):
                        messages.info(request, 'Esta Categoria tiene referencias asociadas ¿Está seguro que desea eliminarla?')
                        #hayDetalles = False

                        for ref in referencias:
                            detalle = DetallesProducto.objects.filter(fkProducto=ref)

                            if((len(detalle) > 0) and (detalle != None)):
                                messages.info(request, 'Esta Categoria tiene productos asociadas ¿Está seguro que desea eliminarla?')
                                break
                
                context={'categorias':categorias,
                        'nombreO':nombreO,
                        'rutaImagenO': "../"+rutaImagenO.name,
                        'idcategoria':int(idcategoria)}

    return render(request,'inventario/categoriasEliminar.html', context,{})

def categoria(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, "inventario/categoria.html",context, {})

def modificar_categoria(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    modificar = request.POST
    idCategoria = "-1"#actualiza combobox
    subCategorias = {}
    nombreCategoria = ""
    rutaImagenO = ""
    idCategoriaSubCat = "-1"
    nombreSubCat = ""
    selectSubCat = "-1"#actualizar combobox subcategoria
    idSubCategoria = "-1"

    context={'categorias':categorias, 'subCategorias':subCategorias, 'idCategoria':int(idCategoriaSubCat), 'nombreCategoria':nombreCategoria, 'rutaImagenO':rutaImagenO}
    if (request.method == 'POST'):
        idCategoria = modificar.get('categoria')
        idCategoriaSubCat = modificar.get('idCat')
        nombreSubCat = modificar.get('nombreSubCategoria')
        accionSubCatSubmit = modificar.get('SubCat-submit')
        acccionModCatSubmit = modificar.get('modfCat-submit')
        selectSubCat = modificar.get('subCategoria')#actualizar combobox subcategoria
        idSubCategoria = modificar.get('idSubCategoria')
        ###################################
        print("idCat ",idCategoria)
        print("idSubCat ",idSubCategoria)

        #modificar categoria
        print("HOLAAA ", acccionModCatSubmit, " - ", idCategoria)
        if ( acccionModCatSubmit == "Modificar" and not(idCategoriaSubCat=='-1' or idCategoriaSubCat==None)):
            nombreCategoria = modificar.get('nombreCategoria')
            categoriaObject = Categoria.objects.get(pkCategoria=idCategoriaSubCat)
            imagen = categoriaObject.rutaImagen
            rutaImagenO = "../"+imagen.name

            imagenModif = False
            
            if((modificar.get('buscadorImagen')!= '')):
                imagen = request.FILES['buscadorImagen']
                imagenModif = True
            
            aux =  Categoria(nombreCategoria = nombreCategoria,
                            rutaImagen = imagen)
            try:
                aux.clean_fields()
                aux.clean()
            except ValidationError as e:
                print(e)
                context={'categorias':categorias, 'subCategorias':subCategorias, 'idCategoria':idCategoriaSubCat, 'nombreCategoria':nombreCategoria, 'rutaImagenO':rutaImagenO}
                messages.info(request, 'Nuevo nombre de categoria invalido')
                return render(request, "inventario/modificar_categoria.html", context, {})

            print("HOLAAA ", nombreCategoria)
            Categoria.objects.filter(pkCategoria = idCategoriaSubCat).update(nombreCategoria = aux.nombreCategoria)
            if(imagenModif):
                    categ = Categoria.objects.get(pkCategoria = idCategoriaSubCat)
                    categ.rutaImagen.save(imagen.name,File(imagen),'r')
            context={'categorias':categorias}
            messages.success(request, 'Categoria modificada exitosamente')
            return render(request, "inventario/modificar_categoria.html", context, {})
        ########################### 

        #agregar subcategoria
        if(accionSubCatSubmit=="Agregar" and not(idCategoriaSubCat=='' or idCategoriaSubCat=='-1' or idCategoriaSubCat==None)):
            print("solicitudcorrecta")
            aux = SubCategoria(
                fkCategoria=Categoria.objects.get(pkCategoria=idCategoriaSubCat),
                nombreSubCategoria=nombreSubCat
            )
            try:
                aux.full_clean()
            except ValidationError as e:
                context={'categorias':categorias}
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                return render(request, "inventario/modificar_categoria.html", context, {})
            aux.save()
            context={'categorias':categorias}
            messages.success(request, 'SubCategoria agregada con exito')
            return render(request, "inventario/modificar_categoria.html", context, {})
        #########################

        #modificar subcategoria
        if(accionSubCatSubmit=="Modificar" and not(idCategoriaSubCat=='' or idSubCategoria=='-1' or idSubCategoria==None)):
            try:
                idCat = SubCategoria.objects.filter(pkSubCategoria = idSubCategoria).first()
                aux = SubCategoria(
                    fkCategoria= idCat.fkCategoria,
                    nombreSubCategoria=nombreSubCat
                ) 
                aux.full_clean()
            except ValidationError as e:
                context={'categorias':categorias}
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                return render(request, "inventario/modificar_categoria.html", context, {})
            SubCategoria.objects.filter(pkSubCategoria = idSubCategoria).update(nombreSubCategoria = aux.nombreSubCategoria)
            context={'categorias':categorias}
            messages.success(request, 'SubCategoria modificada con exito')
            return render(request, "inventario/modificar_categoria.html", context, {})        
        #########################

        #eliminar subcategoria
        if(accionSubCatSubmit=="Eliminar" and not(idCategoriaSubCat=='' or idSubCategoria=='-1' or idSubCategoria==None)):
            try:
                idCat = SubCategoria.objects.filter(pkSubCategoria = idSubCategoria)
            except ValidationError as e:
                context={'categorias':categorias}
                messages.info(request, 'Por favor seleccione una subcategoria')
                return render(request, "inventario/modificar_categoria.html", context, {})
            SubCategoria.objects.filter(pkSubCategoria = idSubCategoria).delete()
            context={'categorias':categorias}
            messages.success(request, 'SubCategoria eliminada con exito')
            return render(request, "inventario/modificar_categoria.html", context, {})   
        ##########################3

        #actualiza combobox categoria 
        subCategorias = {}
        subCat = ""
        nombreCategoria = ""
        nombreSubCategoria = ""
        if(idCategoria !='-1' and idCategoria != None):
            categoriaObject = Categoria.objects.get(pkCategoria=idCategoria)    
            nombreCategoria = categoriaObject.nombreCategoria
            rutaImagenO = "../"+categoriaObject.rutaImagen.name
            subCategorias = SubCategoria.objects.filter(fkCategoria=idCategoria)
        if (selectSubCat != '-1' and selectSubCat != None):
            subCat = SubCategoria.objects.filter(pkSubCategoria = selectSubCat)
            #print(subCat.nombreSubCategoria)
            nombreSubCategoria = subCat[0].nombreSubCategoria
        #actualiza combobox subcategoria
        if(idCategoria==None): idCategoria = "-1"
        context={'categorias':categorias, 'subCategorias':subCategorias, 'idCategoria':int(idCategoria), 'nombreCategoria':nombreCategoria, 'rutaImagenO':rutaImagenO,'idSubCategoria': selectSubCat, 'nombreSubCategoria': nombreSubCategoria}
    return render(request, "inventario/modificar_categoria.html", context, {})

@csrf_protect
def aniadirCategoria(request, *args, **kwargs):
    context={}
    if (request.method == 'POST'):
        datos = request.POST
        nombre = datos.get('nombreCategoria')
        imagen = request.FILES['buscadorImagen']
        if((imagen!= None) and (nombre!="")):
            aux = Categoria( nombreCategoria = nombre,
                             rutaImagen = imagen,
            )
            aux.rutaImagen.save(imagen.name,File(imagen),'r')
            try:
                aux.full_clean()
            except ValidationError as e:
                messages.info(request, 'Alguno(s) campo(s) no son validos')

            aux.save()
            messages.success(request, 'Categoria agregada con exito')

    return render(request, "inventario/categoriaCrear.html", {})

def productos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, "inventario/productos.html",context, {})

def productosCrearPrincipal(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, "inventario/productosCrearPrincipal.html",context, {})

def aniadirReferencias(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    idCategoria = 0
    subCategorias = {}

    if(request.method == 'POST'):
        modificar = request.POST
        idCategoria = modificar.get('categoria')
        submitReq = modificar.get('productos-submit')

        subCategorias = {}
        if(idCategoria=='-1' or idCategoria==None):
            idCategoria = -1
            subCategorias = {}
        else:
            categoriaObject = Categoria.objects.get(pkCategoria=idCategoria)    
            subCategorias = SubCategoria.objects.filter(fkCategoria=idCategoria)

        #CREAR REFERENCIAS ------------------------------------
        idSubCat = modificar.get('subCategoria')
        nombre = modificar.get('inputNombre')
        descripcion = modificar.get('DescrProducto')
        precio = 0
        iva = 0
        
        if(modificar.get('inputPrecio')!="" and modificar.get('inputPrecio')!=None):
            precio = int(modificar.get('inputPrecio'))    
        if(modificar.get('inputIva')!="" and modificar.get('inputIva')!=None):
            iva = int(modificar.get('inputIva'))
        if(submitReq=="Crear Referencia" and not(idSubCat=="null") and not(nombre=="") and not(descripcion=="") and not(iva<=0) and not(precio<=0)):
            #print(imagen)
            imagen = request.FILES['buscadorImagen']#####
            aux = Producto(
                fkSubCategoria = SubCategoria.objects.get(pkSubCategoria=idSubCat),
                nombre = nombre,
                descripcion = descripcion,
                iva = iva,
                precio = precio,
                rutaImagen = imagen
            )
            aux.rutaImagen.save(imagen.name,File(imagen),'r')
            try:
                aux.full_clean()
            except ValidationError as e:
                context={'categorias':categorias, 'idCategoria':int(idCategoria), 'subCategorias':subCategorias}
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                return render(request, "inventario/referenciasCrear.html", context, {})
            #aux.rutaImagen.save()
            aux.save()
            context={'categorias':categorias, 'idCategoria':int(idCategoria), 'subCategorias':subCategorias}
            messages.success(request, 'Referencia creada con exito')
            return render(request, "inventario/referenciasCrear.html", context, {})
        elif(submitReq=="Crear Producto"):
            context={'categorias':categorias, 'idCategoria':int(idCategoria), 'subCategorias':subCategorias}
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "inventario/referenciasCrear.html", context, {})

    context={'categorias':categorias, 'idCategoria':int(idCategoria), 'subCategorias':subCategorias}
    return render(request, "inventario/referenciasCrear.html", context, {})

def aniadirProductos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()
    bodegas = Bodega.objects.all()
    idCategoria = 0
    subCategorias = {}

    if(request.method == 'POST'):
        modificar = request.POST  
        submitReq = modificar.get('productos-submit')

        #AGREGAR PRODUCTOS ----------------------------------------------
        idProducto = modificar.get('producto')
        idProveedor = modificar.get('proveedor')
        idBodega = modificar.get('bodega')
        talla = modificar.get('talla')
        cantidad = 0
        if(modificar.get('inputCant')!="" and modificar.get('inputCant')!=None):
            cantidad = int(modificar.get('inputCant'))
        color = modificar.get('inputColor')

        if(submitReq=="Agregar Productos" and not(idProducto=="-1") and not(idProveedor=="-1") and not(idBodega=="-1") and not(talla=="") and not(color=="") and not(cantidad<=0)):
            aux = DetallesProducto(
                fkProducto = Producto.objects.get(pkProducto=idProducto),
                talla = talla,
                nit = Proveedor.objects.get(pknit=idProveedor),
                color = color,
                fkBodega = Bodega.objects.get(pkBodega=idBodega),
                cantidad = cantidad,
            )        
            try:
                aux.full_clean()
            except ValidationError as e:
                context={'categorias':categorias, 'idCategoria':idCategoria, 'subCategorias':subCategorias, 'productos':productos, 'proveedores':proveedores, 'bodegas':bodegas}
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                return render(request, "inventario/productosCrear.html", context, {})

            aux.save()
            context={'categorias':categorias, 'idCategoria':idCategoria, 'subCategorias':subCategorias, 'productos':productos, 'proveedores':proveedores, 'bodegas':bodegas}
            messages.success(request, 'Productos agregados con exito')
            return render(request, "inventario/productosCrear.html", context, {})
        elif(submitReq=="Agregar Productos"):
            context={'categorias':categorias, 'idCategoria':idCategoria, 'subCategorias':subCategorias, 'productos':productos, 'proveedores':proveedores, 'bodegas':bodegas}
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "inventario/productosCrear.html", context, {})

    context={'categorias':categorias, 'idCategoria':idCategoria, 'subCategorias':subCategorias, 'productos':productos, 'proveedores':proveedores, 'bodegas':bodegas}
    return render(request, "inventario/productosCrear.html", context, {})

def productosModificarPrincipal(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, "inventario/productosModificarPrincipal.html",context, {})

def modificarReferencias(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    modificar = request.POST
    idcategoria = modificar.get('categoria')
    subcategorias = {}
    idsubcategoria = modificar.get('subcategoria')
    productos = {}
    idproducto = modificar.get('producto')
    catSeleccionada = False
    subCatSeleccionada = False
    producSeleccionado = False
    
    if((modificar.get('categoria') != "") and (modificar.get('categoria') != None) and (modificar.get('categoria') != "-1")):
        subcategorias = SubCategoria.objects.filter(fkCategoria=idcategoria)
        catSeleccionada = True
    else:
        idcategoria = -1

    if((modificar.get('subcategoria') != "") and (modificar.get('subcategoria') != None) and (modificar.get('subcategoria') != "-1")):
        productos = Producto.objects.filter(fkSubCategoria=idsubcategoria)
        subCatSeleccionada = True
    else:
        idsubcategoria = -1
    
    if((modificar.get('producto') != "") and (modificar.get('producto') != None) and (modificar.get('producto') != "-1")):                
        idproducto = modificar.get('producto')
        producSeleccionado = True
    else:
        idproducto = -1

    context={
        'categorias':categorias,
        'subcategorias':subcategorias, 
        'productos':productos,
        'idcategoria':int(idcategoria),
        'idsubcategoria':int(idsubcategoria),
        'idproducto':int(idproducto),
        'nombreO': "",
        'idO': "",
        'descripcionO': "",
        'ivaO': "",
        'precioO': "",
        'rutaImagenO': "",
    }

    if (modificar.get('productos-submit')=="Modificar Referencia"): #SE MODIFICA LA REFERENCIA
        nombre = modificar.get('inputNombre')
        descripcion = modificar.get('DescrProducto')
        precio = 0
        iva = 0
        if(modificar.get('inputPrecio')!="" and modificar.get('inputPrecio')!=None):
            precio = int(modificar.get('inputPrecio'))
        if(modificar.get('inputIva')!="" and modificar.get('inputIva')!=None):
            iva = int(modificar.get('inputIva'))
        
        imagenModif = False
        idP = modificar.get('inputId')
        producObject = Producto.objects.get(pkProducto=idP)
        imagen = producObject.rutaImagen
        
        if((modificar.get('buscadorImagen')!= '')):
            imagen = request.FILES['buscadorImagen']
            imagenModif = True

        if(producSeleccionado and not(nombre=="") and not(descripcion=="") and not(iva<=0) and not(precio<=0) and not(imagen=="")): #catSeleccionada and subCatSeleccionada and 
            nombreCategoria = modificar.get('nombreCategoria')
            aux = Producto(                
                fkSubCategoria = SubCategoria.objects.get(pkSubCategoria=idsubcategoria),
                nombre = nombre,
                descripcion = descripcion,
                iva = iva,
                precio = precio,
                rutaImagen = imagen
            )
            #if(imagenModif):
                #save(imagen.name,File(imagen),'r')
            try:
                aux.full_clean()
            except ValidationError as e:
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                context={
                    'categorias':categorias,
                    'subcategorias':subcategorias, 
                    'productos':productos,
                    'idcategoria':int(idcategoria),
                    'idsubcategoria':int(idsubcategoria),
                    'idproducto':int(idproducto),
                    'nombreO': aux.nombre,
                    'idO': int(modificar.get('inputId')),
                    'descripcionO': aux.descripcion,
                    'ivaO': modificar.get('inputIva'),
                    'precioO': aux.precio,
                    'rutaImagenO': "../"+imagen.name,
                }
                return render(request, "inventario/referenciasModificar.html", context, {})

            Producto.objects.filter(pkProducto = idproducto).update(
                                                                nombre = aux.nombre,
                                                                descripcion = aux.descripcion,
                                                                iva = aux.iva,
                                                                precio = aux.precio,
                                                                rutaImagen = aux.rutaImagen
                                                            )
            if(imagenModif):
                product = Producto.objects.get(pkProducto = idproducto)
                product.rutaImagen.save(imagen.name,File(imagen),'r')                
            messages.success(request, 'Referencia modificada exitosamente')
            context={
                'categorias':categorias,
                'subcategorias':subcategorias, 
                'productos':productos,
                'idcategoria':int(idcategoria),
                'idsubcategoria':int(idsubcategoria),
                'idproducto':int(idproducto),
                'nombreO': aux.nombre,
                'idO': int(modificar.get('inputId')),
                'descripcionO': aux.descripcion,
                'ivaO': modificar.get('inputIva'),
                'precioO': aux.precio,
                'rutaImagenO': "../"+imagen.name,
            }
            return render(request, "inventario/referenciasModificar.html", context, {})

        else:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            context={
                'categorias':categorias,
                'subcategorias':subcategorias, 
                'productos':productos,
                'idcategoria':int(idcategoria),
                'idsubcategoria':int(idsubcategoria),
                'idproducto':int(idproducto),
                'nombreO': nombre,
                'idO': int(modificar.get('inputId')),
                'descripcionO': descripcion,
                'ivaO': modificar.get('inputIva'),
                'precioO': precio,
                'rutaImagenO': "../"+imagen.name,
            }
            return render(request, "inventario/referenciasModificar.html", context, {})

    elif((idproducto != "") and (idproducto != None) and (idproducto != "-1") and (idproducto != -1)): #SE CARGAN LOS VALORES DE LA REFERENCIA
        producObject = Producto.objects.get(pkProducto=idproducto)
        nombreO = producObject.nombre
        descripcionO = producObject.descripcion        
        precioO = producObject.precio
        ivaO = producObject.iva
        #ivaO = int(math.ceil((ivaOPorcent*100)/precioO))
        rutaImagenO = producObject.rutaImagen

        context={
            'categorias':categorias,
            'subcategorias':subcategorias, 
            'productos':productos,
            'idcategoria':int(idcategoria),
            'idsubcategoria':int(idsubcategoria),
            'idproducto':int(idproducto),
            'nombreO': nombreO,
            'idO': int(idproducto),
            'descripcionO': descripcionO,
            'ivaO': int(ivaO),
            'precioO': precioO,
            'rutaImagenO': "../"+rutaImagenO.name,
        }
    return render(request, "inventario/referenciasModificar.html", context, {})

def modificarProductos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    idProducto = 0
    proveedores = Proveedor.objects.all()
    idProveedor = 0
    bodegas = Bodega.objects.all()
    idBodega = 0

    detalles = {}
    idDetalle = 0

    #Variables de carga de campos
    referenciaO = ""
    idrefO= 0
    tallaO = ""
    nitO = ""
    colorO = ""
    fkBodegaO = ""
    cantidadO = 0

    if(request.method == 'POST'):
        modificar = request.POST
        #if((modificar.get('producto') != None) and (modificar.get('producto') != "") and (modificar.get('producto') != "-1")):
        idProducto = int(modificar.get('producto'))
        idProveedor = modificar.get('proveedor')
        idBodega = int(modificar.get('bodega'))

        #BUSCAR DETALLES
        if((idProducto!=-1) and (idProveedor!="-1") and (idBodega!=-1)): #LOS TRES CAMPOS SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor,
                                                        fkBodega=idBodega)
        elif((idProducto!=-1) and (idProveedor!="-1")):  #PRODUCTO Y PROVEEDOR SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor)
        elif((idProducto!=-1) and (idBodega!=-1)):     #PRODUCTO Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        fkBodega=idBodega)
        elif((idProveedor!="-1") and (idBodega!=-1)):    #PROVEEDOR Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(nit=idProveedor,
                                                        fkBodega=idBodega)
        else: #SOLO UN CAMPO SELECC
            if(idProducto!=-1):    #PRODUCTO SELECCIONADO
                detalles = DetallesProducto.objects.filter(fkProducto=idProducto)
            elif(idProveedor!="-1"): #PROVEEDOR SELECCIONADO
                detalles = DetallesProducto.objects.filter(nit=idProveedor)
            elif(idBodega!=-1):    #BODEGA SELECCIONADA
                detalles = DetallesProducto.objects.filter(fkBodega=idBodega)


        #MODIFICAR EL PRODUCTO
        if((modificar.get('productos-submit')=="Modificar Producto") and (modificar.get('detalle') != None) and (modificar.get('detalle') != "") and (modificar.get('detalle') != "-1")):
            idDetalle = int(modificar.get('detalle'))

            referencia = int(modificar.get('idref'))
            talla = modificar.get('inputTalla')
            nit = modificar.get('inputProveedor')
            color = modificar.get('inputColor')
            PkBodega = int(modificar.get('inputBodega'))
            cantidad = int(modificar.get('inputCant'))

            aux = DetallesProducto(
                fkProducto = Producto.objects.get(pkProducto=referencia),
                talla = talla,
                nit = Proveedor.objects.get(pknit=nit),
                color = color,
                fkBodega = Bodega.objects.get(pkBodega=PkBodega),
                cantidad = cantidad
            )
            try:
                aux.full_clean()
            except ValidationError as e:
                
                messages.info(request, 'Cantidad invalida')
                context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':idDetalle, 'referencia':aux.fkProducto.nombre, 'idref':aux.fkProducto.pkProducto, 'talla':talla, 'nit':nit, 'color':color, 'pkBodega':PkBodega, 'cantidad':cantidad}
                return render(request, "inventario/productosModificar.html",context, {})

            DetallesProducto.objects.filter(pkDetallesP = idDetalle).update(cantidad = aux.cantidad)

            messages.success(request, 'Producto modificado exitosamente')
            context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':idDetalle, 'referencia':aux.fkProducto.nombre, 'idref':aux.fkProducto.pkProducto, 'talla':aux.talla, 'nit':nit, 'color':aux.color, 'pkBodega':PkBodega, 'cantidad':aux.cantidad}
            return render(request, "inventario/productosModificar.html",context, {})

        #OBTENER LOS CAMPOS ANTIGUOS
        elif((modificar.get('detalle') != None) and (modificar.get('detalle') != "") and (modificar.get('detalle') != "-1")):
            idDetalle = int(modificar.get('detalle'))
            
            detalleObject = DetallesProducto.objects.get(pkDetallesP=idDetalle)
            
            referenciaO = detalleObject.fkProducto.nombre
            idrefO = detalleObject.fkProducto.pkProducto
            tallaO = detalleObject.talla
            nitO = detalleObject.nit.pknit
            colorO = detalleObject.color
            fkBodegaO = detalleObject.fkBodega.pkBodega
            cantidadO = detalleObject.cantidad

    context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':idDetalle, 'referencia':referenciaO, 'idref':idrefO, 'talla':tallaO, 'nit':nitO, 'color':colorO, 'pkBodega':fkBodegaO, 'cantidad':cantidadO}
    #print(context)
    return render(request, "inventario/productosModificar.html",context, {})

def productosConsultarPrincipal(request, *args, **kwargs):
    #categorias = Categoria.objects.all()
    #context={'categorias':categorias}
    return render(request, "inventario/productosConsultarPrincipal.html", {})

def consultarReferencias(request, *args, **kwargs):
    categorias = Categoria.objects.all()

    modificar = request.POST
    idcategoria = modificar.get('categoria')
    subcategorias = {}
    idsubcategoria = modificar.get('subcategoria')
    productos = {}
    idproducto = modificar.get('producto')
    catSeleccionada = False
    subCatSeleccionada = False
    producSeleccionado = False
    
    if((modificar.get('categoria') != "") and (modificar.get('categoria') != None) and (modificar.get('categoria') != "-1")):
        subcategorias = SubCategoria.objects.filter(fkCategoria=idcategoria)
        catSeleccionada = True
    else:
        idcategoria = -1

    if((modificar.get('subcategoria') != "") and (modificar.get('subcategoria') != None) and (modificar.get('subcategoria') != "-1")):
        productos = Producto.objects.filter(fkSubCategoria=idsubcategoria)
        subCatSeleccionada = True
    else:
        idsubcategoria = -1
    
    if((modificar.get('producto') != "") and (modificar.get('producto') != None) and (modificar.get('producto') != "-1")):                
        idproducto = modificar.get('producto')
        producSeleccionado = True
    else:
        idproducto = -1

    context={
        'categorias':categorias,
        'subcategorias':subcategorias, 
        'productos':productos,
        'idcategoria':int(idcategoria),
        'idsubcategoria':int(idsubcategoria),
        'idproducto':int(idproducto),
        'nombreO': "",
        'idO': "",
        'descripcionO': "",
        'ivaO': "",
        'precioO': "",
        'rutaImagenO': "",
    }

    if((idproducto != "") and (idproducto != None) and (idproducto != "-1") and (idproducto != -1)): #SE CARGAN LOS VALORES DE LA REFERENCIA
        producObject = Producto.objects.get(pkProducto=idproducto)
        nombreO = producObject.nombre
        descripcionO = producObject.descripcion        
        precioO = producObject.precio
        ivaO = producObject.iva
        #ivaO = int(math.ceil((ivaOPorcent*100)/precioO))
        rutaImagenO = producObject.rutaImagen

        context={
            'categorias':categorias,
            'subcategorias':subcategorias, 
            'productos':productos,
            'idcategoria':int(idcategoria),
            'idsubcategoria':int(idsubcategoria),
            'idproducto':int(idproducto),
            'nombreO': nombreO,
            'idO': int(idproducto),
            'descripcionO': descripcionO,
            'ivaO': int(ivaO),
            'precioO': precioO,
            'rutaImagenO': "../"+rutaImagenO.name,
        }

    return render(request, "inventario/referenciasConsultar.html", context, {})

def consultarProductos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    idProducto = 0
    proveedores = Proveedor.objects.all()
    idProveedor = 0
    bodegas = Bodega.objects.all()
    idBodega = 0

    detalles = {}
    idDetalle = 0

    #Variables de carga de campos
    referenciaO = ""
    idrefO= 0
    tallaO = ""
    nitO = ""
    colorO = ""
    fkBodegaO = ""
    cantidadO = 0

    if(request.method == 'POST'):
        modificar = request.POST
        idProducto = int(modificar.get('producto'))
        idProveedor = modificar.get('proveedor')
        idBodega = int(modificar.get('bodega'))

        #BUSCAR DETALLES
        if((idProducto!=-1) and (idProveedor!="-1") and (idBodega!=-1)): #LOS TRES CAMPOS SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor,
                                                        fkBodega=idBodega)
        elif((idProducto!=-1) and (idProveedor!="-1")):  #PRODUCTO Y PROVEEDOR SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor)
        elif((idProducto!=-1) and (idBodega!=-1)):     #PRODUCTO Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        fkBodega=idBodega)
        elif((idProveedor!="-1") and (idBodega!=-1)):    #PROVEEDOR Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(nit=idProveedor,
                                                        fkBodega=idBodega)
        else: #SOLO UN CAMPO SELECC
            if(idProducto!=-1):    #PRODUCTO SELECCIONADO
                detalles = DetallesProducto.objects.filter(fkProducto=idProducto)
            elif(idProveedor!="-1"): #PROVEEDOR SELECCIONADO
                detalles = DetallesProducto.objects.filter(nit=idProveedor)
            elif(idBodega!=-1):    #BODEGA SELECCIONADA
                detalles = DetallesProducto.objects.filter(fkBodega=idBodega)


        #OBTENER LOS CAMPOS ANTIGUOS
        if((modificar.get('detalle') != None) and (modificar.get('detalle') != "") and (modificar.get('detalle') != "-1")):
            idDetalle = int(modificar.get('detalle'))
            
            detalleObject = DetallesProducto.objects.get(pkDetallesP=idDetalle)
            
            referenciaO = detalleObject.fkProducto.nombre
            idrefO = detalleObject.fkProducto.pkProducto
            tallaO = detalleObject.talla
            nitO = detalleObject.nit.pknit
            colorO = detalleObject.color
            fkBodegaO = detalleObject.fkBodega.pkBodega
            cantidadO = detalleObject.cantidad

    context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':idDetalle, 'referencia':referenciaO, 'idref':idrefO, 'talla':tallaO, 'nit':nitO, 'color':colorO, 'pkBodega':fkBodegaO, 'cantidad':cantidadO}
    return render(request, "inventario/productosConsultar.html",context, {})

def productosEliminarPrincipal(request, *args, **kwargs):
    return render(request, "inventario/productosEliminarPrincipal.html", {})

def eliminarReferencias(request, *args, **kwargs):
    categorias = Categoria.objects.all()

    modificar = request.POST
    idcategoria = modificar.get('categoria')
    subcategorias = {}
    idsubcategoria = modificar.get('subcategoria')
    productos = {}
    idproducto = modificar.get('producto')
    catSeleccionada = False
    subCatSeleccionada = False
    producSeleccionado = False
    hayProductos = False
    
    if((modificar.get('categoria') != "") and (modificar.get('categoria') != None) and (modificar.get('categoria') != "-1")):
        subcategorias = SubCategoria.objects.filter(fkCategoria=idcategoria)
        catSeleccionada = True
    else:
        idcategoria = -1

    if((modificar.get('subcategoria') != "") and (modificar.get('subcategoria') != None) and (modificar.get('subcategoria') != "-1")):
        productos = Producto.objects.filter(fkSubCategoria=idsubcategoria)
        subCatSeleccionada = True
    else:
        idsubcategoria = -1
    
    if((modificar.get('producto') != "") and (modificar.get('producto') != None) and (modificar.get('producto') != "-1")):                
        idproducto = modificar.get('producto')
        producSeleccionado = True
    else:
        idproducto = -1

    context={
        'categorias':categorias,
        'subcategorias':subcategorias, 
        'productos':productos,
        'idcategoria':int(idcategoria),
        'idsubcategoria':int(idsubcategoria),
        'idproducto':int(idproducto),
        'nombreO': "",
        'idO': "",
        'descripcionO': "",
        'ivaO': "",
        'precioO': "",
        'rutaImagenO': "",
        'hayProductos': hayProductos
    }


    if (modificar.get('productos-submit')=="Eliminar Referencia"): #SE Elimina LA REFERENCIA
        if(producSeleccionado):
            try:
                Producto.objects.filter(pkProducto = idproducto).delete()
            except ValidationError as e:
                messages.info(request, 'Referencia no registrada en el sistema')
                context={
                    'categorias':categorias,
                    'subcategorias':subcategorias, 
                    'productos':productos,
                    'idcategoria':int(idcategoria),
                    'idsubcategoria':int(idsubcategoria),
                    'idproducto':-1,
                    'nombreO': "",
                    'idO': 0,
                    'descripcionO': "",
                    'ivaO': "",
                    'precioO': 0,
                    'rutaImagenO': "",
                    'hayProductos': False
                }
                return render(request, "inventario/referenciasModificar.html", context, {})
                 
            messages.success(request, 'Referencia eliminada exitosamente')
            context={
                'categorias':categorias,
                'subcategorias':subcategorias, 
                'productos':productos,
                'idcategoria':int(idcategoria),
                'idsubcategoria':int(idsubcategoria),
                'idproducto':-1,
                'nombreO': "",
                'idO': 0,
                'descripcionO': "",
                'ivaO': "",
                'precioO': 0,
                'rutaImagenO': "",
                'hayProductos': False
            }
            return render(request, "inventario/referenciasEliminar.html", context, {})

        else:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            context={
                'categorias':categorias,
                'subcategorias':subcategorias, 
                'productos':productos,
                'idcategoria':int(idcategoria),
                'idsubcategoria':int(idsubcategoria),
                'idproducto':int(idproducto),
                'nombreO': nombre,
                'idO': int(modificar.get('inputId')),
                'descripcionO': descripcion,
                'ivaO': modificar.get('inputIva'),
                'precioO': precio,
                'rutaImagenO': "../"+imagen.name,
                'hayProductos': hayProductos
            }
            return render(request, "inventario/referenciasEliminar.html", context, {})

    #SE CARGAN LOS VALORES DE LA REFERENCIA
    elif((idproducto != "") and (idproducto != None) and (idproducto != "-1") and (idproducto != -1)):
        producObject = Producto.objects.get(pkProducto=idproducto)
        nombreO = producObject.nombre
        descripcionO = producObject.descripcion        
        precioO = producObject.precio
        ivaO = producObject.iva
        #ivaO = int(math.ceil((ivaOPorcent*100)/precioO))
        rutaImagenO = producObject.rutaImagen
        detallesP = DetallesProducto.objects.filter(fkProducto=idproducto)

        if((len(detallesP) > 0) and (detallesP != None)):
            #hayProductos = True
            messages.info(request, 'Esta referencia tiene productos asociados ¿Está seguro que desea eliminarla?')

        context={
            'categorias':categorias,
            'subcategorias':subcategorias, 
            'productos':productos,
            'idcategoria':int(idcategoria),
            'idsubcategoria':int(idsubcategoria),
            'idproducto':int(idproducto),
            'nombreO': nombreO,
            'idO': int(idproducto),
            'descripcionO': descripcionO,
            'ivaO': int(ivaO),
            'precioO': precioO,
            'rutaImagenO': "../"+rutaImagenO.name,
            'hayProductos': hayProductos
        }

    return render(request, "inventario/referenciasEliminar.html", context, {})

def eliminarProductos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    idProducto = 0
    proveedores = Proveedor.objects.all()
    idProveedor = 0
    bodegas = Bodega.objects.all()
    idBodega = 0

    detalles = {}
    idDetalle = 0

    #Variables de carga de campos
    referenciaO = ""
    idrefO= 0
    tallaO = ""
    nitO = ""
    colorO = ""
    fkBodegaO = ""
    cantidadO = 0

    if(request.method == 'POST'):
        modificar = request.POST
        idProducto = int(modificar.get('producto'))
        idProveedor = modificar.get('proveedor')
        idBodega = int(modificar.get('bodega'))

        #BUSCAR DETALLES
        if((idProducto!=-1) and (idProveedor!="-1") and (idBodega!=-1)): #LOS TRES CAMPOS SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor,
                                                        fkBodega=idBodega)
        elif((idProducto!=-1) and (idProveedor!="-1")):  #PRODUCTO Y PROVEEDOR SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        nit=idProveedor)
        elif((idProducto!=-1) and (idBodega!=-1)):     #PRODUCTO Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(fkProducto=idProducto,
                                                        fkBodega=idBodega)
        elif((idProveedor!="-1") and (idBodega!=-1)):    #PROVEEDOR Y BODEGA SELECCIONADOS
            detalles = DetallesProducto.objects.filter(nit=idProveedor,
                                                        fkBodega=idBodega)
        else: #SOLO UN CAMPO SELECC
            if(idProducto!=-1):    #PRODUCTO SELECCIONADO
                detalles = DetallesProducto.objects.filter(fkProducto=idProducto)
            elif(idProveedor!="-1"): #PROVEEDOR SELECCIONADO
                detalles = DetallesProducto.objects.filter(nit=idProveedor)
            elif(idBodega!=-1):    #BODEGA SELECCIONADA
                detalles = DetallesProducto.objects.filter(fkBodega=idBodega)


        #ELIMINAR EL PRODUCTO
        if((modificar.get('productos-submit')=="Eliminar Producto") and (modificar.get('detalle') != None) and (modificar.get('detalle') != "") and (modificar.get('detalle') != "-1")):
            idDetalle = int(modificar.get('detalle'))
            try:
                DetallesProducto.objects.filter(pkDetallesP = idDetalle).delete()
            except ValidationError as e:
                messages.info(request, 'Producto no registrado en el sistema')
                context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':-1, 'referencia':"", 'idref':0, 'talla':"", 'nit':"", 'color':"", 'pkBodega':"", 'cantidad':0}
                return render(request, "inventario/productosEliminar.html",context, {})

            messages.success(request, 'Producto eliminado exitosamente')
            context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':-1, 'referencia':"", 'idref':0, 'talla':"", 'nit':"", 'color':"", 'pkBodega':"", 'cantidad':0}
            return render(request, "inventario/productosEliminar.html",context, {})

        #OBTENER LOS CAMPOS ANTIGUOS
        elif((modificar.get('detalle') != None) and (modificar.get('detalle') != "") and (modificar.get('detalle') != "-1")):
            idDetalle = int(modificar.get('detalle'))
            
            detalleObject = DetallesProducto.objects.get(pkDetallesP=idDetalle)
            
            referenciaO = detalleObject.fkProducto.nombre
            idrefO = detalleObject.fkProducto.pkProducto
            tallaO = detalleObject.talla
            nitO = detalleObject.nit.pknit
            colorO = detalleObject.color
            fkBodegaO = detalleObject.fkBodega.pkBodega
            cantidadO = detalleObject.cantidad

            if(cantidadO >0):
                messages.info(request, 'Este producto tiene unidades registradas ¿Está seguro que desea eliminarlo?')

    context={'categorias':categorias, 'productos':productos, 'idProducto':idProducto, 'proveedores':proveedores, 'idProveedor':idProveedor, 'bodegas':bodegas, 'idBodega':idBodega, 'detalles':detalles, 'idDetalle':idDetalle, 'referencia':referenciaO, 'idref':idrefO, 'talla':tallaO, 'nit':nitO, 'color':colorO, 'pkBodega':fkBodegaO, 'cantidad':cantidadO}
    return render(request, "inventario/productosEliminar.html",context, {})

def proveedor(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request, "inventario/proveedor.html",context, {})

def aniadirProveedor(request, *args, **kwargs):
    nit = ""
    direccion = ""
    telefono = ""    
    if request.method == 'POST':
        crear = request.POST
        nit = crear.get('nitProveedor')
        direccion = crear.get('direccionProveedor')
        telefono = crear.get('telefonoProveedor')
        aux = Proveedor( pknit = nit, direccion = direccion, telefono = telefono)
        try:
            aux.full_clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            context={'nit':nit, 'direccion':direccion, 'telefono':telefono}
            return render(request, "inventario/proveedorCrear.html",context,{})
        aux.save()
        messages.success(request, 'Proveedor agregado con exito')
        context={'nit':"", 'direccion':"", 'telefono':""}
        return render(request, "inventario/proveedorCrear.html",context,{})
    context={'nit':nit, 'direccion':direccion, 'telefono':telefono}
    return render(request, "inventario/proveedorCrear.html",context ,{})


def modificarProveedor(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()

    context={'categorias': categorias, 'proveedores': proveedores, 'nit': '', 'telefono': '', 'direccion': ''}
    modificar = request.POST
    nit = modificar.get('nitProveedor')
    actualNit = modificar.get('nit')
    acccionModProveedorSubmit = modificar.get('modificarProveedor-submit')

    #Seleccionar el primer proveedor con el nit si existe
    objectProveedor = Proveedor.objects.filter(pknit = nit).first()
    
    if ( acccionModProveedorSubmit == "Modificar"):
        if (actualNit == ''):
            messages.info(request, 'Seleccione el NIT del proveedor que desea actualizar')
            return render(request, "inventario/proveedorModificar.html",context,{})
        
        telefonoNuevo = modificar.get('telefonoProveedor')
        direccionNueva = modificar.get('direccionProveedor')
        
        
        aux = Proveedor( pknit = actualNit, direccion = direccionNueva, telefono = telefonoNuevo)
        
        try:
            #No se puede full_clean debido a que no seria una clave unica en el modelo su nit
            aux.clean_fields()
            aux.clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "inventario/proveedorModificar.html",context,{})
        Proveedor.objects.filter(pknit = actualNit).update(direccion=direccionNueva, telefono = telefonoNuevo)
        messages.success(request, 'El proveedor ha sido actualizado correctamente')
        return render(request, "inventario/proveedorModificar.html",context,{})

    if (nit != "no elegido" and nit != None):
        telefono = objectProveedor.telefono
        direccion = objectProveedor.direccion
    else:
        nit = ''
        telefono = ''
        direccion = ''
    context={'categorias': categorias, 'proveedores': proveedores, 'nit': nit, 'telefono': telefono, 'direccion': direccion}
    
    return render(request, "inventario/proveedorModificar.html", context, {})

def eliminarProveedor(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    context={'categorias': categorias, 'proveedores': proveedores}
    if request.method == 'POST':
        modificar = request.POST
        nit = modificar.get('nitProveedor')
        print(nit)
        if(nit !=  "no elegido"):
            Proveedor.objects.filter(pknit = nit).delete()
        else:
            messages.info(request, 'Por favor seleccione un proveedor')
            return render(request, "inventario/proveedorEliminar.html",context,{})
        messages.success(request, 'El proveedor ha sido eliminado correctamente')
        return render(request, "inventario/proveedorEliminar.html",context,{})
        
    return render(request, "inventario/proveedorEliminar.html", context, {})


def productosCategoriasVista(request, nombre, categoria):
    categorias = Categoria.objects.all()
    subCategorias=SubCategoria.objects.filter(fkCategoria=categoria)
    context={'categorias':categorias, 'subCategorias':subCategorias, 'categoria':categoria, 'nombre':nombre}
    return render(request, 'inventario/productoCategoriaVista.html', context, {})

def productosSubCategoriasVista(request, nombre, categoria ,subCategoria):
    import datetime
    categorias = Categoria.objects.all()
    subCategorias= SubCategoria.objects.filter(fkCategoria=categoria)
    #
    hoy = datetime.date.today()
    aux = Producto(subCategorias[0].pkSubCategoria, "","", 0.0,0.0)
    #productos con precio cambiado
    productos = aux.productosConDescuento(subCategoria, hoy)
    finales = []
    #productos con detallesproducto o no
    for producto in productos:
        detallesProducto = DetallesProducto.objects.filter(fkProducto = producto)
        
        if detallesProducto:
            finales.append(producto)

    context={'categorias':categorias, 'subCategorias':subCategorias, 'productos': finales, 'categoria':categoria, 'nombre':nombre}
    return render(request, 'inventario/productoCategoriaVista.html', context, {})

def productoDetalles(request, nombre,categoria, idproducto, precio):
    from usuarios.models import Carrito
    import datetime
    esCliente = (nombre != "noRegistrado")
    categorias = Categoria.objects.all()
    auxcategoria = Categoria.objects.get(pkCategoria = categoria)
    subCategorias= SubCategoria.objects.filter(fkCategoria=auxcategoria)
    #subtotal
    subtotal= 1*precio
    # producto
    producto = Producto.objects.get(pkProducto = idproducto)
    detallesProducto = DetallesProducto.objects.filter(fkProducto = producto)
    
    idDetalleproducto = detallesProducto.first().pkDetallesP
    sdp = detallesProducto.get(pkDetallesP = idDetalleproducto)
    # cargar informacion del detalle
    if request.method == 'POST':
        seleccionado = request.POST
        idDetalleproducto = int(seleccionado.get('detalleproducto'))
        sdp = detallesProducto.get(pkDetallesP = idDetalleproducto)
        agregarACarrito = seleccionado.get('AgregarCarrito-submit')
        #agregar a carrito
        if (agregarACarrito == 'AgregarCarrito'):
            try:
                cantidadcomprar = int(seleccionado.get('cantidad'))
            except:
                messages.info(request, 'Cantidad de productos invalidos')
                context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto,'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
                return render(request,'inventario/productoDetalles.html',context,{})
            if (cantidadcomprar > sdp.cantidad):
                messages.info(request, 'No hay esa cantidad de productos disponibles, intente una menor')
                context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto,'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
                return render(request,'inventario/productoDetalles.html',context,{})
            cliente = Cliente.objects.get(nombre = nombre)
            if (cantidadcomprar <= 0):
                messages.info(request, 'Seleccione una cantidad de productos mayor a 0')
                context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto,'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
                return render(request,'inventario/productoDetalles.html',context,{})
            #verificar si ya hay productos de este tipo en el carrito para acumular
            carritoActual = Carrito.objects.filter(fkNombreCliente = nombre)
            print(carritoActual)
            if (carritoActual != None):
                for c in carritoActual:
                    if (c.fkDetalleProducto == sdp):
                        if (c.cantidad + cantidadcomprar > sdp.cantidad):
                            #se quieren acumular mas elementos de los que hay en inventario
                            messages.info(request, 'Cantidad de articulos solicitado mayor al que hay en inventario')
                            context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto,'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
                            return render(request,'inventario/productoDetalles.html',context,{})
                        Carrito.objects.filter(pkCarrito = c.pkCarrito).update(cantidad = c.cantidad + cantidadcomprar)
                        messages.success(request, 'Producto agregado al carrito')
                        context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto,'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
                        return render(request,'inventario/productoDetalles.html',context,{})
            carrito = Carrito(fkNombreCliente = cliente, fkDetalleProducto = sdp, cantidad = cantidadcomprar, precioActual=precio)
            try:
                carrito.full_clean()
            except ValidationError as e:
                messages.info(request, 'Cantidad de articulos  invalida')
                context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto, 'subtotal':subtotal, 'detallesproducto':detallesProducto, 'idDetalleproducto':idDetalleproducto, 'precio':precio, 'productoS':sdp, 'nombre':nombre, 'esCliente':esCliente}
                return render(request,'inventario/productoDetalles.html',context,{})
            carrito.save()
            messages.success(request, 'Producto agregado al carrito')
        
    context={'categorias':categorias,'categoria':categoria, 'subCategorias':subCategorias, 'producto':producto, 'subtotal':subtotal, 'detallesproducto':detallesProducto,'idDetalleproducto':idDetalleproducto,'precio':precio, 'productoS':sdp,'nombre':nombre, 'esCliente':esCliente}
    return render(request, 'inventario/productoDetalles.html', context, {})


def modificarBodega(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    bodegas = Bodega.objects.all()

    context={'categorias': categorias, 'bodegas': bodegas, 'direccion': '', 'ciudad': ''}
    modificar = request.POST
    idB = modificar.get('idBodega')
    actualId = modificar.get('idB')
    acccionModBodegaSubmit = modificar.get('modificarBodega-submit')
    #Seleccionar la bodega
    objectBodega = Bodega.objects.filter(pkBodega = idB).first()
    
    if ( acccionModBodegaSubmit == "Modificar"):
        if (actualId == ''):
            messages.info(request, 'Seleccione la bodega que desea actualizar')
            return render(request, "inventario/bodegaModificar.html",context,{})
  
        ciudadNueva = modificar.get('ciudadBodega')
        direccionNueva = modificar.get('direccionBodega')
        
        
        aux = Bodega(actualId, direccionNueva, ciudadNueva)
        
        try:
            aux.clean_fields()
            aux.clean()
        except ValidationError as e:
            print(request.POST)
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "inventario/bodegaModificar.html",context,{})
        Bodega.objects.filter(pkBodega = actualId).update(direccion=direccionNueva, ciudad = ciudadNueva)
        messages.success(request, 'La bodega ha sido actualizado correctamente')
        return render(request, "inventario/bodegaModificar.html",context,{})

    if (idB != '0' and idB != None):
        ciudad = objectBodega.ciudad
        direccion = objectBodega.direccion
    else:
        idB = ''
        ciudad = ''
        direccion = ''
    ciudades = {
        '',
        'BOG',
        'MED',
        'CALI',
        'B/Q',
        'CART',
        'CUC',
        'SOL',
        'IBG',
        'BCM',
        'SOAC'
    }
    context={'categorias': categorias, 'bodegas': bodegas, 'idB': idB, 'ciudad': ciudad, 'direccion': direccion, 'ciudades':ciudades}
    
    return render(request, "inventario/bodegaModificar.html", context, {})