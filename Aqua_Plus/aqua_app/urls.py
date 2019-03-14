from django.urls import path
from aqua_app import views

urlpatterns=[
	path('',views.index,name="index"),
    path('venta',views.venta,name="venta")
]