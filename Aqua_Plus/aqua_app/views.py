from django.shortcuts import render
from .models import TipoVenta,Usuario
# Create your views here.
def index(request):
	return render(request,'index.html')

def venta(request):
    tipoVenta=TipoVenta.objects.all()
    return render(request,'venta.html',{'venta':tipoVenta})
	
