from django.db import models
import hashlib
from django.core.validators import RegexValidator
from inventario.models import DetallesProducto

class Cliente(models.Model):
    TIPO_DOC = {  
        ('PAS','Pasaporte'),
        ('CC','Cedula de Ciudadania'), 
        ('TI','Tarjeta de Identidad'),
    }

    nombre = models.CharField(max_length=128, unique=True, primary_key=True)
    clave = models.CharField(max_length=128, editable=True)
    fechaNacimiento = models.DateField()
    direccion = models.CharField(max_length=32) 
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{7,10}$', message="El telefono debe tener formato: '+7777777'. Up to 10 digits allowed.")
    telefono = models.CharField(validators=[telefono_regex], max_length=12, blank=True) # validators should be a list
    tipoDocumento = models.CharField(max_length=3, choices = TIPO_DOC)
    numeroDocumento = models.IntegerField()

    #super().save(*args, **kwargs) para guardar en esta tabla
    def save(self, *args, **kwargs):
        self.clave = hashlib.md5(self.clave.encode('utf-8')).hexdigest()
        super(Cliente, self).save(*args, **kwargs)

    def autenticarCliente(self, *args, **kwargs):
        auth = Cliente.objects.filter(nombre=self.nombre,
                                    clave=hashlib.md5(self.clave.encode('utf-8')).hexdigest()).exists()
        return auth

    def buscarCliente(self, *args, **kwargs):
        aux = Cliente.objects.filter(nombre=self.nombre,
                                    clave=hashlib.md5(self.clave.encode('utf-8')).hexdigest())
        return aux

class AdministradorDuenio (models.Model):
    TIPO = {
        ('ADMIN','Administrador'),
        ('CEO','Duenio'),
    }
    pkAdministradorDuenio = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=128, unique=True)
    clave = models.CharField(max_length=128, editable=True)
    tipo = models.CharField(max_length=5, choices=TIPO) 

    #super().save(*args, **kwargs) para guardar en esta tabla
    def save(self, *args, **kwargs):        
        self.clave = hashlib.md5(self.clave.encode('utf-8')).hexdigest()
        super(AdministradorDuenio, self).save(*args, **kwargs)

    def autenticarAdmin(self, *args, **kwargs):
        auth = AdministradorDuenio.objects.filter(nombreUsuario=self.nombreUsuario, clave=hashlib.md5(self.clave.encode('utf-8')).hexdigest(), tipo='ADMIN').exists()
        return auth

    def autenticarDuenio(self, *args, **kwargs):
        auth = AdministradorDuenio.objects.filter(nombreUsuario=self.nombreUsuario, clave=hashlib.md5(self.clave.encode('utf-8')).hexdigest(), tipo='CEO').exists()
        return auth

#ProductosEnCarrito
class Carrito(models.Model):
    pkCarrito = models.AutoField(primary_key=True)
    fkNombreCliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fkDetalleProducto =  models.ForeignKey(DetallesProducto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioActual = models.FloatField()