#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path
from .views import home,galeria,formulario,contactanos,carro

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORMU'),
    path('contactanos/',contactanos,name='CONTA'),  
    path('carro',carro,name='CARRO'),
]