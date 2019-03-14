from django.contrib import admin

# Register your models here.
from .models import Usuario,TipoVenta,Venta
admin.site.register(Usuario)
admin.site.register(TipoVenta)
admin.site.register(Venta)