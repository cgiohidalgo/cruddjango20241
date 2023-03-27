from django.contrib import admin
from .models import Factura, DetallesFactura, DescuentoCategoria, DescuentoSubCategoria, DescuentoProducto, PagosCredito, PagosDebito
# Register your models here.

admin.site.register(Factura)
admin.site.register(DetallesFactura)
admin.site.register(DescuentoCategoria)
admin.site.register(DescuentoSubCategoria)
admin.site.register(DescuentoProducto)
admin.site.register(PagosCredito)
admin.site.register(PagosDebito)
