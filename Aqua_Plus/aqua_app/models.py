from django.db import models

# Create your models here.
# Create your models here.
class Usuario(models.Model):
    correo=models.CharField(max_length=50)
    contrasena=models.CharField(max_length=50)
    tipo=models.IntegerField(default=1)
    def __str__(self):
        return str(self.correo)

class TipoVenta(models.Model):
    tipo=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.tipo)

class Venta(models.Model):
    vendedor=models.ForeignKey('Usuario', on_delete=models.CASCADE,null=True)
    fecha=models.DateTimeField(auto_now_add=True)
    cantidad=models.IntegerField(default=1)
    tipo=models.ForeignKey('TipoVenta', on_delete=models.CASCADE)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.fecha)
