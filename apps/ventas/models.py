from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from inventario.models import Producto, DetallesProducto, Categoria, SubCategoria
from usuarios.models import Cliente

#DescuentoProducto
class DescuentoProducto(models.Model):
    pkDescuentoProducto = models.AutoField(primary_key=True)
    fkProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    fechaInicio = models.DateField(default=timezone.now)
    fechaFin = models.DateField() 
    porcentajeDescuento = models.FloatField(
    validators=[MinValueValidator(1), MaxValueValidator(99)],
)

#DescuentoCategoria
class DescuentoCategoria(models.Model): 
    pkDescuentoCategoria = models.AutoField(primary_key=True)
    fkCategoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL, null=True)
    fechaInicio = models.DateField(default=timezone.now)
    fechaFin = models.DateField()
    porcentajeDescuento = models.FloatField(
    validators=[MinValueValidator(0), MaxValueValidator(99)],
)


#DescuentoSubCategoria
class DescuentoSubCategoria(models.Model):
    pkDescuentoSubCategoria = models.AutoField(primary_key=True)
    fkSubCategoria = models.ForeignKey(SubCategoria,on_delete=models.SET_NULL, null=True)
    fechaInicio = models.DateField(default=timezone.now)
    fechaFin = models.DateField()
    porcentajeDescuento = models.FloatField(
    validators=[MinValueValidator(1), MaxValueValidator(99)],
)

#Factura
class Factura(models.Model):
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
    pkFactura = models.AutoField(primary_key=True)
    fkCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)####################
    ciudad = models.CharField(max_length=4, choices = CIUDAD, default='CALI')
    direccion = models.CharField(max_length=32)
    fecha = models.DateField()

#Detalles Factura
class DetallesFactura(models.Model):
    fkFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fkDetallesP = models.ForeignKey(DetallesProducto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    precio = models.FloatField()

#PagosCredito
class PagosCredito(models.Model):
    ENTIDAD = {
        ('VI','VISA'),
        ('CA','MASTERCARD'),
        ('AX','AMERICANEXPRESS'),
    }
    pkPagosCredito = models.AutoField(primary_key=True)
    fkFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    numeroAprobacion = models.CharField(max_length=32) #donde se genera automatico?
    cuotas = models.FloatField([MinValueValidator(1), MaxValueValidator(36)],)
    fechaAprobacion = models.DateField()
    entidadAprobacion = models.CharField(max_length=2,choices=ENTIDAD)
    porcentajePago = models.FloatField([MinValueValidator(1), MaxValueValidator(99)],
)
#classDebito
class PagosDebito(models.Model):
    pkPagosDebito = models.AutoField(primary_key=True)
    numeroTarjetaDebito = models.IntegerField()#min_length=16
    fkFactura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    ahorros = models.BooleanField()
    porcentajePago = models.FloatField([MinValueValidator(1), MaxValueValidator(99)],
)