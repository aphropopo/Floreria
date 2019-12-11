#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('contactanos/',contactanos,name='CONTA'),  
    path('carro',carro,name='CARRO'),
    path('login/',login,name='LOGIN'),
    path('login_iniciar/',login_iniciar,name='LOGIN_INICIAR'),
    path('cerrar_sesion/',cerrar_sesion,name='CERRAR_SESION'),
    path('registro/',registro,name='REGISTRO'),
    path('agregar_carro/<id>/',agregar_carro,name='AGREGAR_CARRO'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR_FLOR'),
    path('vaciar_carrito/',vacio_carrito,name='VACIARCARRITO'),
]