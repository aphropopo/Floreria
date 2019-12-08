#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path
from .views import home,galeria,formulario,contactanos,carro,login,login_iniciar,cerrar_sesion,registro

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
]