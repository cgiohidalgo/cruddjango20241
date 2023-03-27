from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

#Categoria
class Categoria(models.Model):
    pkCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=256, unique=True)
    rutaImagen = models.ImageField(upload_to = '../media/categoriasImagenes')###############

#Subcategoria
class SubCategoria(models.Model):
    pkSubCategoria = models.AutoField(primary_key=True)
    fkCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombreSubCategoria = models.CharField(max_length=256, unique=True)


#Producto
class Producto(models.Model):
    pkProducto = models.AutoField(primary_key=True)
    fkSubCategoria = models.ForeignKey(SubCategoria, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=300, default = "null")
    descripcion = models.CharField(max_length=1024)
    iva = models.FloatField( default=0, validators=[MinValueValidator(0), MaxValueValidator(99)],)
    precio = models.IntegerField()
    rutaImagen = models.ImageField(upload_to = '../media/productosImagenes')###############

    #toma todos los productos dados
    #retorna lista de productos con el precio cambiado, si tiene al menos un descuento activo
    #si tienen mas de uno toma el mayor
    #sino retorna el mismo objeto con solamente el iva aplicado
    def productosConDescuento(self,subCategoria,hoy,*args, **kwargs):
        from ventas.models import DescuentoProducto, DescuentoCategoria, DescuentoSubCategoria
        #descuento activos para la fecha presente
        descuentosProductos = DescuentoProducto.objects.filter(fechaFin__gte=hoy).filter(fechaInicio__lte=hoy)
        descuentosCategorias = DescuentoCategoria.objects.filter(fechaFin__gte=hoy).filter(fechaInicio__lte=hoy)
        descuentosSubCategorias = DescuentoSubCategoria.objects.filter(fechaFin__gte=hoy).filter(fechaInicio__lte=hoy)
        #inicializando las variables
        productosConDp = []
        productosConDsc = []
        productosConDc = []
        #productos con descuento de producto
        for dp in descuentosProductos:
            #si el descuento es de mi subcategoria
            auxproducto = Producto.objects.get(pkProducto = dp.fkProducto.pkProducto)
            auxsubcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria)
            if (auxproducto.fkSubCategoria != auxsubcategoria):
                continue
            else:
                productosConDp = Producto.objects.filter(pkProducto = dp.fkProducto.pkProducto)
        #productos con descuento de subcategoria
        for dsc in descuentosSubCategorias:
            #si el descuento en que estoy es de mi subcategoria
            if (dsc.fkSubCategoria.pkSubCategoria != int(subCategoria)):
                continue
            else:
                #obtengo los productos de mi subcategoria
                productosConDsc = Producto.objects.filter(fkSubCategoria=subCategoria)
        #productos con descuento de categoria
        for dc in descuentosCategorias:
            #si el descuento en que estoy es de mi categoria
            if (dc.fkCategoria != SubCategoria.objects.get(pkSubCategoria = subCategoria).fkCategoria):
                continue
            else:
                #obtengo los productos de mi categoria
                productosConDc = Producto.objects.filter(fkSubCategoria=subCategoria)
        #vemos si los productos existentes tienen alguno de los descuentos recolectados        
        productos = Producto.objects.filter(fkSubCategoria=subCategoria)
        resultado = []
        ##¿el operador in en python cuesta O(n) en el peor caso deberiamos hacer hash? o no se si se puede la verdad
        for producto in productos:
            if ((producto not in productosConDp) and (producto not in productosConDsc) and (producto not in productosConDc)):
                #se adiciona iva, no tienen ningun descuento
                producto.precio = producto.precio + (producto.precio * (producto.iva * 0.01))
                resultado.append(producto)
                continue
            elif ((producto in productosConDp) and (producto in productosConDsc) and (producto in productosConDc)):
                #encontrar el mayor descuento y aplicarlo
                #descuento por producto
                d1 = descuentosProductos.filter(fkProducto = producto).order_by("porcentajeDescuento").first()
                #descuento por categoria
                auxcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria).fkCategoria
                d2 = descuentosCategorias.filter(fkCategoria = auxcategoria).order_by('porcentajeDescuento').first()
                #descuento por subcategoria
                auxsubcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria)
                d3 = descuentosSubCategorias.filter(fkSubCategoria = auxsubcategoria).order_by('porcentajeDescuento').first()
                #cual es el mayor de los 3
                maxDescuento = max(d1.porcentajeDescuento, d2.porcentajeDescuento, d3.porcentajeDescuento)
                producto.precio = producto.precio + (producto.precio * (producto.iva * 0.01)) - (producto.precio * (maxDescuento * 0.01))
                resultado.append(producto)
            elif ((producto in productosConDp) and (producto in productosConDsc)):
                #encontrar el mayor descuento y aplicarlo
                d1 = descuentosProductos.filter(fkProducto = producto).order_by("porcentajeDescuento").first()
                #descuento por subcategoria
                auxsubcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria)
                d3 = descuentosSubCategorias.filter(fkSubCategoria = auxsubcategoria).order_by('porcentajeDescuento').first()
                #maximo
                maxDescuento = max(d1.porcentajeDescuento, d3.porcentajeDescuento)
                producto.precio = producto.precio + (producto.precio * (producto.iva * 0.01)) - (producto.precio * (maxDescuento * 0.01))
                resultado.append(producto)
            elif ((producto in productosConDp) and (producto in productosConDc)):
                #encontrar el mayor descuento y aplicarlo
                d1 = descuentosProductos.filter(fkProducto = producto).order_by("porcentajeDescuento").first()
                #descuento por categoria
                auxcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria).fkCategoria
                d2 = descuentosCategorias.filter(fkCategoria = auxcategoria).order_by('porcentajeDescuento').first()
                #maximo
                maxDescuento = max(d1.porcentajeDescuento, d2.porcentajeDescuento)
                producto.precio = producto.precio + (producto.precio * (producto.iva * 0.01)) - (producto.precio * (maxDescuento * 0.01))
                resultado.append(producto) 
            elif ((producto in productosConDsc) and (producto in productosConDc)):
                #encontrar el mayor descuento y aplicarlo
                #descuento por subcategoria
                auxsubcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria)
                d3 = descuentosSubCategorias.filter(fkSubCategoria = auxsubcategoria).order_by('porcentajeDescuento').first()
                #descuento por categoria
                auxcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria).fkCategoria
                d2 = descuentosCategorias.filter(fkCategoria = auxcategoria).order_by('porcentajeDescuento').first()
                #maximo
                maxDescuento = max(d2.porcentajeDescuento, d3.porcentajeDescuento)
                producto.precio = producto.precio + (producto.precio * (producto.iva * 0.01)) - (producto.precio * (maxDescuento * 0.01))
                resultado.append(producto) 
            elif(producto in productosConDp):
                #solo tiene descuento por producto se aplica junto al iva
                p = descuentosProductos.get(fkProducto = producto)
                producto.precio = producto.precio - (producto.precio * (p.porcentajeDescuento * 0.01)) + (producto.precio * (producto.iva * 0.01))
                resultado.append(producto)
                continue
            elif(producto in productosConDsc):
                #solo tiene descuento por subcategoria se aplica junto al iva
                auxsubcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria)
                p = descuentosSubCategorias.filter(fkSubCategoria = auxsubcategoria).order_by('porcentajeDescuento').first()
                producto.precio = producto.precio - (producto.precio * (p.porcentajeDescuento * 0.01)) + (producto.precio * (producto.iva * 0.01))
                resultado.append(producto)
                continue
            elif(producto in productosConDc):
                #solo tiene descuento por categoria se aplica junto al iva
                auxcategoria = SubCategoria.objects.get(pkSubCategoria = subCategoria).fkCategoria
                p = descuentosCategorias.filter(fkCategoria = auxcategoria).order_by('porcentajeDescuento').first()
                producto.precio = producto.precio - (producto.precio * (p.porcentajeDescuento * 0.01)) + (producto.precio * (producto.iva * 0.01))
                resultado.append(producto)
                continue

        return resultado



#Proveedor
class Proveedor(models.Model):
    pknit = models.CharField(primary_key=True, max_length=16)
    direccion = models.CharField(max_length=128)
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{7,10}$', message="El telefono debe tener formato: '+7777777'. Up to 10 digits allowed.")
    telefono = models.CharField(validators=[telefono_regex], max_length=12, blank=True)

#Bodega
class Bodega(models.Model):
    CIUDAD = {
        ('BOG','Bogotá'),
        ('MED','Medellín'),
        ('CALI','Cali'),
        ('B/Q','Barranquilla'),
        ('CART','Cartagena'),
        ('CUC','Cucuta'),
        ('SOL','Soledad'),
        ('IBG','Ibague'),
        ('BCM','Bucaramanga'),
        ('SOAC','Soacha'),
    }
    pkBodega = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=4, choices = CIUDAD, default='CALI')


#DetallesProducto
class DetallesProducto(models.Model):            
    COLOR = {
        ('Negro',' Negro'),
        ('Blanco','Blanco'),
        ('Amarillo','Amarillo'),
        ('Azul','Azul'),
        ('Rojo','Rojo'),
        ('Verde','Verde'),
        ('Morado','Morado'),
        ('Naranja','Naranja'),
        ('Rosado','Rosado'),
        ('Gris','Gris'),
        ('Marron','Marrón'),
        ('Beige','Beige'),
        ('Otros','Otro'),
    }
    TALLA = {
        ('XS','xs'),
        ('S','s'),
        ('M','m'),                  
        ('L','l'),
        ('XL','xl'),
    }
    pkDetallesP = models.AutoField(primary_key=True)
    fkProducto =  models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    talla = models.CharField(max_length=32, choices=TALLA)
    nit = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=64, choices=COLOR)
    fkBodega = models.ForeignKey(Bodega, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()

