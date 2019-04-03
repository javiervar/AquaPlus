from django.urls import path
from aqua_app import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
	path('',views.index,name="index"),
    path('venta/',views.venta,name="venta"),
    path('adminView/',views.adminView,name="adminView"),
    path('getTipoVenta/',views.GetTipoVenta.as_view(),name="getTipoVenta"),
    path('usuarios/',views.Usuarios.as_view(),name="usuarios"),
    path('eliminarUsuario/',views.EliminarUsuario.as_view(),name="eliminarUsuario"),
    path('login/',views.Login.as_view(),name="login"),
    path('vender/',views.VentaView.as_view(),name="venta"),
    path('reportes/',views.VentaView.as_view(),name="venta"),
]