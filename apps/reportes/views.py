from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from ventas.models import *
from inventario.models import *
from usuarios.models import *
from datetime import timedelta, date, datetime
from dateutil import relativedelta

# Create your views here.

def masVendidos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    
    productos = DetallesFactura.objects.values('fkDetallesP__fkProducto__fkSubCategoria__nombreSubCategoria', 'fkDetallesP__fkProducto__fkSubCategoria__fkCategoria__nombreCategoria', 'fkDetallesP__fkProducto__pkProducto', 'fkDetallesP__fkProducto__nombre').annotate(total=Sum('cantidad')).order_by('-total')[:20]
    
    context={'categorias':categorias, 'productos': productos, 'masOMenos': 'Más'}
    return render(request, 'reportes/vendidos.html', context, {})

    

def menosVendidos(request, *args, **kwargs):
    categorias = Categoria.objects.all()
    
    productos = DetallesFactura.objects.values('fkDetallesP__fkProducto__fkSubCategoria__nombreSubCategoria', 'fkDetallesP__fkProducto__fkSubCategoria__fkCategoria__nombreCategoria', 'fkDetallesP__fkProducto__pkProducto', 'fkDetallesP__fkProducto__nombre').annotate(total=Sum('cantidad')).order_by('total')[:20]
    
    context={'categorias':categorias, 'productos': productos, 'masOMenos': 'Menos'}
    return render(request, 'reportes/vendidos.html', context, {})



def inicioReportes(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        data = request.POST
        reporte = data.get('tipoReporte')
        url = 'reportes:'+reporte
        return redirect(to=url)
    return render (request, "reportes/reportes.html", context, {})

def daterangeday(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def daterangemonth(start_date, end_date):
    r = relativedelta.relativedelta(end_date, start_date).months
    for n in range(r):
        yield start_date + relativedelta.relativedelta(months=+n)

def daterangeyear(start_date, end_date):
    r = relativedelta.relativedelta(end_date, start_date).years
    for n in range(r):
        yield start_date + relativedelta.relativedelta(years=+n)

def reporteVentas(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        data = request.POST
        fechaInicio = ""
        fechaFin = ""
        try:
            fechaInicio = datetime.strptime(data.get('fecha_inicio'), '%Y-%m-%d')
            fechaFin = datetime.strptime(data.get('fecha_fin'), '%Y-%m-%d')
        except:
            messages.info(request, 'Por favor ingrese una fecha valida')
            return render(request, "reportes/reporteVentas.html", context, {})
        tipoReporte = int(data.get('tipoReporte'))
        dias = []
        cantidad = []
        if (tipoReporte==1):
            cant = 0
            for dia in daterangeday(fechaInicio, fechaFin):
                cant = Factura.objects.filter(fecha=dia).count()
                cantidad.append(cant)
                dias.append(dia.strftime('%Y-%m-%d'))
            context={"datax":dias,"datay":cantidad, "fechaInicio":fechaInicio.strftime('%Y-%m-%d'), "fechaFin":fechaFin.strftime('%Y-%m-%d')}
            return render(request, "reportes/reporteVentas.html", context, {})
        if (tipoReporte==2):
            fechaInicio = date(fechaInicio.year, fechaInicio.month, 1)
            fechaFin = date(fechaFin.year, fechaFin.month, 1)
            for mes in daterangemonth(fechaInicio, fechaFin):
                cant = 0
                for dia in daterangeday(mes, (mes + relativedelta.relativedelta(months=+1)) ):
                    cant += Factura.objects.filter(fecha=dia).count()
                cantidad.append(cant)
                dias.append(mes.strftime('%Y-%m'))
            context={"datax":dias,"datay":cantidad, "fechaInicio":fechaInicio.strftime('%Y-%m'), "fechaFin":fechaFin.strftime('%Y-%m')}
            return render(request, "reportes/reporteVentas.html", context, {})
        if (tipoReporte==3):
            fechaInicio = date(fechaInicio.year, 1, 1)
            fechaFin = date(fechaFin.year, 1, 1) + relativedelta.relativedelta(years=+1)
            for year in daterangeyear(fechaInicio, fechaFin):
                cant = 0
                for dia in daterangeday(year, (year + relativedelta.relativedelta(years=+1)) ):
                    cant += Factura.objects.filter(fecha=dia).count()
                cantidad.append(cant)
                dias.append(year.strftime('%Y'))
            context={"datax":dias,"datay":cantidad, "fechaInicio":fechaInicio.strftime('%Y'), "fechaFin":fechaFin.strftime('%Y')}
            return render(request, "reportes/reporteVentas.html", context, {})

    return render (request, "reportes/reporteVentas.html", context, {})

def reporteProducto(request, *args, **kwargs):
    from django.db.models import Q
    productos = Producto.objects.all()
    context = {'productos':productos}
    if request.method == 'POST':
        data = request.POST
        today = date.today()
        fechaFin = date(today.year, today.month, today.day)
        fechaInicio = fechaFin + relativedelta.relativedelta(months=-6)
        try:
            producto = int(data.get('producto'))
        except:
            messages.info(request, 'Por favor seleccione un producto')
            return render(request, "reportes/reporteProducto.html", context, {})
        dias = []
        cantidad = []
        prod = Producto.objects.get(pkProducto=producto)
        for dia in daterangeday(fechaInicio, fechaFin):
            cant = 0
            detalles_p = DetallesProducto.objects.filter(fkProducto=producto)

            for detalle in detalles_p:
                facturas = Factura.objects.filter(fecha=dia)

                for factura in facturas:
                    cant += DetallesFactura.objects.filter(Q(fkFactura=factura.pkFactura) & Q(fkDetallesP=detalle.pkDetallesP)).count()

            cantidad.append(cant)
            dias.append(dia.strftime('%Y-%m-%d'))
        context={"datax":dias,"datay":cantidad, "fechaInicio":fechaInicio.strftime('%Y-%m-%d'), "fechaFin":fechaFin.strftime('%Y-%m-%d'), 'productos':productos}
        return render(request, "reportes/reporteProducto.html", context, {})
    
    return render (request, "reportes/reporteProducto.html", context, {})

def reporteVentasCategoria(request, *args, **kwargs):
    context = {}
            
    cats = Categoria.objects.all()
    categorias = []
    cantidades = []

    for p in cats:
        categorias.append(p.nombreCategoria)
        cant = 0

        subCats = SubCategoria.objects.filter(fkCategoria=p.pkCategoria)

        for subC in subCats:
            productos = Producto.objects.filter(fkSubCategoria=subC.pkSubCategoria)

            for product in productos:
                detalles = DetallesProducto.objects.filter(fkProducto=product.pkProducto)

                for deta in detalles:
                    detallesFacturas = DetallesFactura.objects.filter(fkDetallesP=deta.pkDetallesP)

                    for detaFact in detallesFacturas:
                        cant = cant + detaFact.cantidad

        cantidades.append(cant)

    context={"datax":categorias,"datay":cantidades}

    if(categorias == []):
        messages.info(request, 'No hay categorías')

    print(context)
    
    return render (request, "reportes/reporteVentasCategoria.html", context, {})


def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key[2] > arr[j][2] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key

    return arr 

def reporteTopClientes(request, *args, **kwargs):
    top = 0
    clientesTop = []    
    clientesTopFinal = []

    if request.method == 'POST':
        datos = request.POST
        topStr = datos.get('top')

        if((topStr!='') and (topStr!=None) and (int(topStr)>0)):
            top = int(topStr)
            clientes = Cliente.objects.all()
            numClientes = clientes.count()

            #Consigue una lista de los clientes con su respectiva cantidad de productos comprada y dinero invertido
            for cliente in clientes:
                totalC = 0
                totalV = 0
                
                facturas = Factura.objects.filter(fkCliente=cliente.nombre)

                for factura in facturas:
                    detalleFactura = DetallesFactura.objects.filter(fkFactura=factura.pkFactura).annotate(totalC=Sum('cantidad'),totalV=Sum('precio'))    

                    if(not(detalleFactura.exists())):
                        continue
                        
                    totalC = totalC + detalleFactura[0].totalC
                    totalV = totalV + detalleFactura[0].totalV
                            
                if(totalC!=0):
                    clientesTop.append([cliente.nombre,totalC,totalV])                
            

            clientesTop = insertionSort(clientesTop) #Organiza la lista del top de mayor a menor

            if(top>numClientes):
                messages.info(request,'Hay menos clientes registrados de los indicados')

            conteo = 0
            conteoTop = top
            if(top>len(clientesTop)):
                conteoTop = len(clientesTop)
                messages.info(request,'Los clientes sin compras son omitidos')
            elif(top>numClientes): conteoTop = numClientes

            #Acomoda la lista del top en el formato para el html
            for Ctop in clientesTop:
                if(Ctop[1]==0):
                    continue

                if(conteo>=conteoTop):
                    break

                clientesTopFinal.append({'nombre':Ctop[0],'cantidad':Ctop[1],'dinero':Ctop[2]})
                conteo = conteo + 1

        else:
            messages.info(request, 'Por favor ingrese una cantidad válida')
        
    context = {'top':top, 'clientes':clientesTopFinal}
    return render (request, "reportes/reporteTopClientes.html", context, {})

    
def reportePocasUnidades(request):
    categorias = Categoria.objects.all()
    ingresar = request.POST

    productos = DetallesProducto.objects.values('fkProducto__nombre', 'color', 'talla').annotate(total=Sum('cantidad')).filter(total__lte=5)
    print(productos.query)
    print(productos)
    
    context={'categorias':categorias, 'productos': productos}
    return render(request, 'reportes/reportePocasUnidades.html', context, {})

def reporteCumpleañosCliente(request):
    import datetime
    hoy = datetime.date.today()
    clientes = Cliente.objects.all()
    salida = []
    for cliente in clientes:
        if (cliente.fechaNacimiento.month == hoy.month):
            salida.append(cliente)
    context={'clientes': salida, 'mes': hoy.strftime('%B')}
    return render(request, 'reportes/reporteCumpleañosClientes.html', context, {})

def reporteProductosCliente(request):
    infocliente = Cliente.objects.all()
    context={'clientes':infocliente, 'datax':[],'datay':[] }
    if (request.method == 'POST'):
        reporte = request.POST
        cliente = reporte.get('clientes')
        if (infocliente != ''):
            facturas = Factura.objects.filter(fkCliente = cliente)
            datax = []
            datay = []
            salida = []
            for factura in facturas:
                aux = DetallesFactura.objects.values('fkDetallesP__fkProducto__nombre', 'cantidad').filter(fkFactura = factura)
                for item in aux:
                    datax.append(item['fkDetallesP__fkProducto__nombre'])
                    datay.append(item['cantidad'])
            print(datax)
            print(datay)
            context = {'clientes':infocliente, 'datax':datax,'datay':datay}
        else:
            messages.info(request, 'No se seleccionó un cliente valido')
    return render(request, 'reportes/reporteProductosClientes.html', context, {})
