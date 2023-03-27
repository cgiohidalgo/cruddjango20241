from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError
from django.utils import timezone
from usuarios.models import *
from ventas.models import *
from inventario.models import Categoria

from django.db import transaction
from datetime import datetime

def clienteIngreso(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    ingresar = request.POST
    context={'categorias':categorias, 'nombre':'noRegistrado'}
    if(request.method == 'POST'):
        aux = Cliente(
            nombre=ingresar.get('username'),
            clave=ingresar.get('password'),
            fechaNacimiento = timezone.now,
            direccion = "",
            telefono = "",
            tipoDocumento = "",
            numeroDocumento = 1234567,
        )
        nombre=ingresar.get('username')
        if (aux.autenticarCliente()):
            context={'categorias':categorias, 'nombre':nombre}
            messages.success(request, f'¡Bienvenido {nombre}!')
            return render(request, 'usuarios/clienteinicio.html', context,{})
        else:
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'usuarios/clienteingreso.html', context,{'form':ingresar})

def clienteCerrarSesion(request, *args, **kwargs):
    return redirect(to='usuarios:ingreso')

def clienteInicio(request, nombre):
    categorias = Categoria.objects.all()
    context={'categorias':categorias, 'nombre': nombre}
    return render(request, 'usuarios/clienteinicio.html', context, {})

@csrf_protect
def clienteregistro(request):
    categorias = Categoria.objects.all()    
    registrar = request.POST
    if(request.method == 'POST'):
        nombre = registrar.get('nombreCliente')
        clave = registrar.get('claveCliente')
        fechaNacimiento = registrar.get('fechaNacimiento')
        direccion = registrar.get('direccionCliente')
        telefono = registrar.get('telefonoCliente')
        tipoDocumento = registrar.get('tipoDocumento')
        numeroDocumento = registrar.get('documentoCliente')        

        auxfechaNac = datetime.strptime(fechaNacimiento,'%Y-%m-%d')
        hoy = datetime.today()
        #print("NAC: ", auxfechaNac, "   Hoy: ", hoy, "    -  ", auxfechaNac>=hoy)
        #print((({auxfechaNac.day} == {hoy.day}) and ({auxfechaNac.month} == {hoy.month})))

        context={'categorias':categorias, 'nombre':'noRegistrado', 'nombrer':nombre, 'clave':clave, 'fechaNacimiento':fechaNacimiento, 'direccion':direccion, 'telefono':telefono, 'tipoDocumento':tipoDocumento, 'numeroDoc':numeroDocumento}

        if((auxfechaNac.year >= hoy.year) and (auxfechaNac.month >= hoy.month) and (auxfechaNac.day >= hoy.day)):
            messages.info(request, 'La fecha no puede ser igual o mayor a la fecha actual')
            return render(request, "usuarios/clienteregistro.html", context,{'form':registrar})
        else:
            aux = Cliente(
                nombre= nombre,
                clave = clave,
                fechaNacimiento = fechaNacimiento,
                direccion = direccion,
                telefono = telefono,
                tipoDocumento = tipoDocumento,
                numeroDocumento = numeroDocumento,
            )
            try:
                aux.full_clean()
            except ValidationError as e:
                messages.info(request, 'Alguno(s) campo(s) no son validos')
                return render(request, "usuarios/clienteregistro.html", context,{'form':registrar})
            nombre =registrar.get('nombreCliente')
            aux.save()
            messages.success(request, f'¡{nombre} bienvenido(a) a Nova!')
            context={'categorias':categorias, 'nombre':'noRegistrado'}
            return redirect(to='usuarios:ingreso')

    context={'categorias':categorias, 'nombre':'noRegistrado'}
    return render(request, "usuarios/clienteregistro.html",context, {'form':registrar})


def paginaPrincipal_admin(request):
    categorias = Categoria.objects.all()
    admin = AdministradorDuenio.objects.get(pkAdministradorDuenio =  1)
    #admin = get_object_or_404(AdministradorDuenio, pkAdministradorDuenio=id_dueno)
    context = {
        'objeto' : admin,
        'categorias': categorias
    }
    return render(request, "usuarios/paginaPrincipal_admin.html",context)

def paginaPrincipal_duenio(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    duenio = AdministradorDuenio.objects.get(pkAdministradorDuenio=1)
    context = {
        'objeto' : duenio,
        'categorias': categorias
    }
    return render(request, "usuarios/paginaPrincipal_duenio.html",context)


def duenioAdminAgregar(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    agregar = request.POST
    if(request.method=='POST'):
        admin=AdministradorDuenio(
            nombreUsuario=agregar.get('nombreAdmin'),
            clave=agregar.get('claveAdmin'),
            tipo='ADMIN'
        )
        try:
            admin.full_clean()
        except ValidationError as e:
            messages.info(request, 'Alguno(s) campo(s) no son validos')
            return render(request, "usuarios/duenioAdminAgregar.html",context,{'form':agregar})
        nombre =agregar.get('nombreAdmin')
        admin.save()
        messages.success(request, f'¡Bienvenido {nombre} !')
        return redirect(to='usuarios:duenioAgregarAdmin')
    return render(request,"usuarios/duenioAdminAgregar.html",context,{'form':agregar})


def adminMenu(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request,"usuarios/adminMenu.html",context, {})


def clienteMenu(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    return render(request,"usuarios/clienteMenu.html",context, {})


def duenioAdminIngreso(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    context={'categorias':categorias}
    ingresar = request.POST
    if(request.method == 'POST'):
        admin = AdministradorDuenio(
            nombreUsuario=ingresar.get('nombreDuenioAdmin'),
            clave=ingresar.get('claveDuenioAdmin'),
            tipo='ADMIN'
        )

        duenio=AdministradorDuenio(
            nombreUsuario=ingresar.get('nombreDuenioAdmin'),
            clave=ingresar.get('claveDuenioAdmin'),
            tipo='CEO'
        )
        nombre=ingresar.get('nombreDuenioAdmin')
        if (admin.autenticarAdmin()):
            messages.success(request, f'¡Bienvenido {nombre}!')
            return redirect(to='usuarios:paginaPrincipal_admin')
        elif (duenio.autenticarDuenio()):
            messages.success(request, f'¡Bienvenido {nombre}!')
            return redirect(to='usuarios:paginaPrincipal_duenio')
        else:
            messages.info(request, 'Cuenta de usuario o contraseña invalida')
    return render(request, 'usuarios/duenioAdminIngreso.html',context,{'form':ingresar})

def duenioAdminModificar(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    usuarios = AdministradorDuenio.objects.filter(tipo='ADMIN')
    context={'categorias':categorias, 'usuarios':usuarios}

    modificar = request.POST
    
    nombreAdmin = modificar.get('nombreEmpleado')
    claveAdmin = modificar.get('claveAdmin')

    if(request.method == 'POST'):
        try:
            print ('Llega a antes de modificar')
            objects = AdministradorDuenio.objects.filter(nombreUsuario = nombreAdmin)
            #Hice la modificación de la clave como atributo para usar save
            #y asi usar el encriptado dentro de la función, en lugar de usar update
            for obj in objects:
                obj.clave = claveAdmin
                obj.save()
            
            messages.success(request, 'Administrador modificado exitosamente')
        except ValidationError as e:
            messages.info(request, 'El usuario administrador no pudo ser modificado')
            
    return render(request, "usuarios/duenioAdminModificar.html", context, {})
    
def duenioAdminEliminar(request, *args, **kwargv):
    categorias = Categoria.objects.all()
    usuarios = AdministradorDuenio.objects.filter(tipo='ADMIN')
    context={'categorias':categorias, 'usuarios':usuarios}
    if(request.method == 'POST'):
        data = request.POST
        idAdmin = data.get('idAdmin')
        AdministradorDuenio.objects.filter(pkAdministradorDuenio=idAdmin).delete()
        messages.success(request, 'El empleado fue despedido exitosamente')
        return render(request, "usuarios/duenioAdminEliminar.html", context, {})
    return render(request, "usuarios/duenioAdminEliminar.html", context, {})

def duenioClienteConsultar(request, *args, **kwargs):
    from django.db.models import Q
    categorias = Categoria.objects.all()
    clientes = {}
    consultar = request.POST
    buscador = consultar.get('buscador')
    if (buscador):
        clientes = Cliente.objects.filter(Q(nombre__icontains=buscador) | Q(direccion__icontains=buscador) | Q(telefono__icontains=buscador) | Q(numeroDocumento__icontains=buscador))
    else:
        clientes = Cliente.objects.all()
    context={'categorias':categorias, 'clientes': clientes}
        
    return render(request, "usuarios/duenioClienteConsultar.html", context, {})

def duenioAdminConsultar(request, *args, **kwargs):
    from django.db.models import Q
    categorias = Categoria.objects.all()
    administradores = {}
    consultar = request.POST
    buscador = consultar.get('buscador')
    if (buscador):
        administradores = AdministradorDuenio.objects.filter(Q(tipo='ADMIN') & (Q(nombreUsuario__icontains=buscador) | Q(pkAdministradorDuenio__icontains=buscador)))
    else:
        administradores = AdministradorDuenio.objects.filter(tipo='ADMIN')
    context={'categorias':categorias, 'clientes': administradores}
        
    return render(request, "usuarios/duenioAdminConsultar.html", context, {})


def clientePerfil(request, nombre):
    cliente = Cliente.objects.filter(nombre=nombre)
    context = {'nombre':nombre, 'cliente':cliente}
    return render(request,"usuarios/clientePerfil.html", context, {})

def clienteHistorialCompras(request, nombre):
    cliente = Cliente.objects.filter(nombre=nombre)

    facturas = Factura.objects.filter(fkCliente=nombre)
    detalles = []

    for factura in facturas:
        detalleFactura = DetallesFactura.objects.filter(fkFactura=factura.pkFactura)        
        total = 0

        for detalleFact in detalleFactura:
            total = total + (detalleFact.precio * detalleFact.cantidad)

        detalles.append({'id':factura.pkFactura, 'fecha':factura.fecha, 'total':total , 'detalle':detalleFactura})


    context = {'nombre':nombre, 'cliente':cliente, 'facturas':detalles}
    return render(request,"usuarios/clienteHistorialCompras.html", context, {})



def clienteCarrito(request, nombre):
    import datetime
    from ventas.models import PagosDebito, PagosCredito, DetallesFactura, Factura
    from django.db import IntegrityError
    
    categorias = Categoria.objects.all()
    accion = request.POST
    idEliminar = accion.get('eliminar')
    tipoTarjeta = accion.get('tipotarjeta')
    #subtotal de productos en carrito
    productosCarrito = Carrito.objects.filter(fkNombreCliente=nombre)
    totalcompra = 0
    cantidadValida = False
    num = {}
    for producto in productosCarrito:
        totalcompra += (producto.precioActual *  producto.cantidad)
    #eliminar producto
    if(idEliminar):
        try:
            Carrito.objects.filter(pkCarrito=idEliminar).delete()
            return redirect('/usuarios/carrito/'+nombre)
        except ValidationError as e:
            messages.info(request, 'El artículo no pudo ser eliminado del carrito')
    #compra transaccional
    #cantidad de tarjetas a utilizar 1, 2 o 3
    try:
        with transaction.atomic():
            numeroDebito = accion.get('cuantasDebito')
            cuantasDebito = {}
            numeroCredito = accion.get('cuantasCredito')
            cuantasCredito = {}
            numTarjetas = accion.get('cuantas')
            if(numTarjetas):
                num = range(1, int(numTarjetas)+1)
            #tipos de tarjetas
            if(numeroDebito or numeroCredito):
                if(( int(numeroDebito) + int(numeroCredito) > 3) or (int(numeroCredito) + int(numeroDebito) == 0)):
                    messages.info(request, 'Error, puede usar maximo 3 tarjetas y minimo 1 tarjeta')
                    raise IntegrityError('numerodebito or numerocredito') 
                else:
                    cantidadValida = True
                    cuantasDebito = range(1, int(numeroDebito)+1)
                    cuantasCredito = range(1, int(numeroCredito)+1)
                    #Significa que uno de los campos no fue llenado pero no es necesario informar, porque pudo ser aproposito si solo se usa un medio de pago

            #recolectando info de tarjetas y destino
            numDebito = accion.getlist('numDebito')
            numCredito = accion.getlist('CnumTarjeta')
            if(numDebito or numCredito):
                if (len(numDebito) + len(numCredito) > 3):
                    messages.info(request, 'Error maximo puede usar 3 tarjetas')
                    raise IntegrityError('maximo 3 tarjetas')
                else:
                    Dporcentaje = accion.getlist('Dporcentaje')
                    Cporcentaje = accion.getlist('Cporcentaje')
                    sumd = sumc = 0
                    #acumular porcentajes de tarjetas
                    for dp in Dporcentaje:
                        sumd += int(dp)
                    for dc in Cporcentaje:
                        sumc += int(dc)
                    #porcentajes que sumen 100
                    if(sumd + sumc  != 100):
                        messages.info(request, 'Error, no se a asignado el total de la venta en los porcentajes de las tarjetas')
                    else:
                        if(len(numCredito) != 0):
                            #haber seleccionado entidades
                            entidades = accion.getlist('entidad')
                            for e in entidades:
                                if(e == '-1'):
                                    messages.info(request, 'Error, no se selecciono una entidad valida')
                                    raise IntegrityError('entidad')
                            cuotas = accion.getlist('Ccuotas')
                            #cuotas validas
                            for c in cuotas:
                                if (int(c) > 36 or int(c) < 1):
                                    messages.info(request, 'Error, cantidad de cuotas invalida')
                                    raise IntegrityError
                            CnumAprobacion = accion.getlist('CnumAprobacion')
                        if (len(numDebito) != 0):
                            #atrapar toda la informacion para crear las tarjetas
                            Dahorros = accion.getlist('Dahorros')
                        hoy =datetime.date.today()
                        direccion = accion.get('direccion')
                        ciudad = accion.get('ciudad')
                        #crear factura general
                        auxCliente = Cliente.objects.get(nombre = nombre)
                        auxFactura = Factura(fkCliente = auxCliente, ciudad = ciudad, direccion = direccion, fecha = hoy)
                        auxFactura.full_clean()
                        auxFactura.save()
                        #crear detalles de factura uno por producto en carrito
                        for item in productosCarrito:
                            auxDetalleproducto = DetallesProducto.objects.get(pkDetallesP = item.fkDetalleProducto.pkDetallesP)
                            auxDetalleFactura = DetallesFactura(fkFactura = auxFactura,
                                                                fkDetallesP = item.fkDetalleProducto,
                                                                cantidad = item.cantidad,
                                                                precio = item.precioActual)   
                            auxDetalleFactura.full_clean()
                            auxDetalleFactura.save()
                        #crear tarjetas usadas
                        #tarjetas debito
                        count = 0
                        if (len(numDebito) != 0):
                            for d in numDebito:
                                auxahorro = False
                                if (Dahorros[count] == '-1'):
                                    raise IntegrityError('Error al escoger el tipo de cuenta')
                                if (Dahorros[count] == 'Ahorros'):
                                    auxahorro = True
                                auxDebito = PagosDebito(numeroTarjetaDebito = d,
                                                        fkFactura = auxFactura,
                                                        porcentajePago = Dporcentaje[count],
                                                        ahorros = auxahorro) 
                                auxDebito.full_clean()
                                auxDebito.save()
                                count+=1
                        #tarjetas credito
                        count = 0
                        if(len(numCredito) != 0):
                            for c in numCredito:
                                auxCredito = PagosCredito(fkFactura = auxFactura,
                                                        numeroAprobacion = CnumAprobacion,
                                                        cuotas = cuotas[count],
                                                        fechaAprobacion = hoy,
                                                        entidadAprobacion = entidades[count],
                                                        porcentajePago = Cporcentaje[count])
                                
                                auxCredito.full_clean()
                                auxCredito.save()
                                count += 1
                        #restar del inventario
                        for item in productosCarrito:
                            auxcantidad = item.cantidad
                            DetallesProducto.objects.filter(pkDetallesP = item.fkDetalleProducto.pkDetallesP).update(cantidad = item.fkDetalleProducto.cantidad  - auxcantidad)
                            #agregar gastos de envio
                            if(item.fkDetalleProducto.fkBodega.ciudad != ciudad):
                                totalcompra += 5000
                        #vaciar el carrito
                        Carrito.objects.filter(fkNombreCliente = auxCliente).delete() #elimino los items en carrito
                        #si todo salio bien
                        messages.success(request, 'Compra realizada exitosamente total: '+str(totalcompra))
                        productosCarrito = {}
    except ValidationError as e:
        messages.info(request, str(e))
    except ValueError as e:
        messages.info(request, "Algun valor numerico dado no es valido")
    except IntegrityError as e:
        pass
    
    context = {'cantidadValida': cantidadValida, 'totalcompra':totalcompra,'categorias':categorias,'nombre': nombre, 'productosCarrito': productosCarrito, 'rangeDebito': cuantasDebito, 'numtarjetas':num, 'numeroDebito': numeroDebito, 'rangeCredito': cuantasCredito, 'numeroCredito': numeroCredito}
    return render(request, "usuarios/clienteCarrito.html", context, {'form':accion})


'''
def handler404(request, exception):
    print('handler 404')
    return render('usuarios/404.html',{},{})

def handler500(request):
    return HttpResponse('error 500 en, nova', status=404)
    '''


def clienteEliminar(request, nombre):

    cliente = Cliente.objects.filter(nombre=nombre)
    
    accion = request.POST
    confirmar = accion.get('confirmar')
    context = {'nombre':nombre, 'cliente':cliente}
    if(confirmar=="si"):
        try:
            Cliente.objects.filter(nombre=nombre).delete()
            messages.warning(request, 'Su cuenta fue eliminada satisfactoriamente')
            return redirect(to='usuarios:ingreso')
        except:
            messages.info(request, 'No fue posible la eliminación de esta cuenta, verifique que se trate de una cuenta registrada')
    if(confirmar=="no"):
        
        return redirect('/usuarios/clientePerfil/'+nombre+'/')

    
    return render(request,"usuarios/clienteEliminar.html", context, {})