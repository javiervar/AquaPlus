from django.shortcuts import render
from .models import TipoVenta,Usuario,Venta
from rest_framework import viewsets,generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest,HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def index(request):
	return render(request,'index.html')

def adminView(request):
	return render(request,'admin.html')

def venta(request):
    tipoVenta=TipoVenta.objects.all()
    return render(request,'venta.html',{'venta':tipoVenta})
	
class GetTipoVenta(APIView):
    def get(self,request):
        tipoVenta=TipoVenta.objects.all()
        response_data={}
        response_data['message'] = serializers.serialize('json', tipoVenta)
        return HttpResponse(JsonResponse(response_data), content_type="application/json")

class VentaView(APIView):
    def post(self,request):
        cantidad=request.data["cantidad"]
        tipoId=request.data["tipo"]
        total=request.data["total"]
        vendedorId=request.data["vendedor"]
        vendedor=Usuario.objects.get(id=vendedorId)
        tipo=TipoVenta.objects.get(id=tipoId)
        Venta(vendedor=vendedor,cantidad=cantidad,tipo=tipo,total=total).save()
        
        return Response({'error':1,'msg':"LA VENTA SE REALIZO CON EXITO"})
    def get(self,request):
        ventas=Venta.objects.all()
        print(ventas)
        retrn=[]
        for value in ventas:
            ret={}
            print(value)
            ret['tipo']=value.tipo.tipo
            ret['id']=value.id
            ret['fecha']=value.fecha
            ret['vendedor']=value.vendedor.correo
            ret['cantidad']=value.cantidad
            ret['total']=value.total
            print(value.vendedor.correo)
            retrn.append(ret)
        print(retrn)
        response_data={}
        response_data['message'] = serializers.serialize('json', ventas)
        return Response(retrn)



class Usuarios(APIView):
    def get(self,request):
        usuarios=Usuario.objects.filter(tipo=2)
        print(usuarios)
        response_data={}
        response_data['message'] = serializers.serialize('json', usuarios)
        return HttpResponse(JsonResponse(response_data), content_type="application/json")
    def post(self,request):
        print(request.data)
        correo=request.data["correo"]
        password=request.data["pass"]
        try:
            usuario = Usuario.objects.get(correo=correo)
        except Usuario.DoesNotExist:
            usuario = None
        if usuario:
            ret={'error':2,'msg':'EL CORREO YA EXISTE'}
        else:
            usuario = Usuario(correo=correo,contrasena=password,tipo=2)
            usuario.save()
            print(usuario)
            ret={'error':1,'msg':'USUARIO GUARDADO'}
        
        return  Response(ret)

class EliminarUsuario(APIView):
	def post(self,request):
		print(request.data)
		usuarioId=request.data["usuario"]
		Usuario.objects.get(id=usuarioId).delete()
		
		return Response({'error':1,'msg':"USUARIO ELIMINADO"})

class Login(APIView):
    def post(self,request):
        print(request.data)
        correo=request.data["correo"]
        password=request.data["pass"]
        try:
            usuario = Usuario.objects.get(correo=correo,contrasena=password)
        except Usuario.DoesNotExist:
            usuario = None
        print(usuario)
        ret={'error':2}
        if usuario:
            ret={'error':1,'correo':usuario.correo,'id':usuario.id,'tipo':usuario.tipo}
        return  Response(ret)