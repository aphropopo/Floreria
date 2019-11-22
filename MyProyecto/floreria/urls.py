#tendra todas las url del sitio web
from django.contrib import admin
from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='Home'),
]