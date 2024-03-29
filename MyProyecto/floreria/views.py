from django.shortcuts import render
from django.contrib.auth.models import User
# importar el sistema de autentificacion
from .models import Flores,Usuario
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth import login,authenticate
# importar los "decorators" que permiten evitar el ingreso a una pagina
# sin estar logeado
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .forms import CustomUserForm

from rest_framework import viewsets
from .serializer import FlorSerializer
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
import json

from fcm_django.models import FCMDevice



# Create your views here. Crea los controladores
#Para las paginas webs
@csrf_exempt
@require_http_methods(['POST'])
def guardar_token(request):
    body = request.body.decode('utf-8')
    bodyDict = json.loads(body)

    token = bodyDict['token']

    existe = FCMDevice.objects.filter(registration_id = token, active = True)

    if len(existe) > 0:
        return HttpResponseBadRequest(json.dumps({'mensaje':'el token ya existe'}))
    
    dispositivo = FCMDevice()
    dispositivo.registration_id = token
    dispositivo.active = True

    if request.user.is_authenticated:
        dispositivo.user = request.user

    try:
        dispositivo.save()
        return HttpResponse(json.dumps({'mensaje':'token guardado'}))
    except:
        return HttpResponseBadRequest(json.dumps({'mensaje':'no se ha podido guardar'}))

@login_required(login_url='/login/')
def home(request):
    return render(request,'core/index.html') 
    #Retorna la pagina renderizada

def login(request):
    return render(request,'registration/login.html')

def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request,'core/index.html')
    return render(request,'registration/login.html')

@login_required(login_url='/login/')
def galeria(request):
    floress=Flores.objects.all()
    return render(request, 'core/galeria.html',{'listaflores':floress})
    #Retorna la pagina renderizada


@login_required(login_url='/login/')
def contactanos(request):
    return render(request, 'core/contactanos.html')
    #Retorna la pagina renderizada

def cerrar_sesion(request):
    logout(request)
    return render(request,'core/cerrar_sesion.html')

@login_required(login_url='/login/')
def carro(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carro.html",{'lista':arr})

@login_required(login_url='/login/')
def vacio_carrito(request):
    request.session["carro"]=""
    lista=request.session.get("carro","")
    return render(request,"core/carro.html",{'lista':lista})

@login_required(login_url='/login/')
def agregar_carro(request, id):
    flores=Flores.objects.filter(name__contains=id)
    valor=Flores.valor   
    sesion=request.session.get("carro","")
    arr=sesion.split(";")
    arr2=''
    sw=0
    cant=1
    for f in arr:
        pel=f.split(":")        
        if pel[0]==id:
            cant=int(pel[1])+1
            sw=1
            arr2=arr2+str(pel[0])+":"+str(cant)+";"            
        elif not pel[0]=="":
            cant=pel[1]
            arr2=arr2+str(pel[0])+":"+str(cant)+";"
    if sw==0:
        arr2=arr2+str(id)+":"+str(cant)+";"

    request.session["carro"]=arr2

    flor=Flores.objects.all()

    msg='Se agrego'
    return render(request, 'core/galeria.html',{'listaflores':flor,'msg':msg})

@login_required(login_url='/login/')
def carrito(request):
    lista=request.session.get("carro","")
    arr=lista.split(";")
    return render(request,"core/carrito.html",{'lista':arr})

@permission_required('core.delete_flores')
def eliminar_flor(request,id):
    msg=''    
    flores=Flores.objects.get(name=id)
    try:
        flores.delete()
        msg='Flor Eliminada'
    except:
        msg='No Pudo Eliminar Flor'
    flor=Flores.objects.all()
    return render(request, 'core/galeria.html',{'listaflores':flor,'msg':msg})
    

def registro(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
        
            
    return render(request, 'registration/registro.html', data)
    #Retorna la pagina renderizada

@permission_required('core.add_flores')
def formulario(request):
    if request.POST:
        name=request.POST.get("txtName")
        valor=request.POST.get("txtValor")
        descripcion=request.POST.get("txtDescripcion")
        stock=request.POST.get("txtStock")
        #recuperar la imagen desde el formulario
        imagen=request.FILES.get("txtImagen")
        #crear una instancia de Pelicula (modelo)
        flor=Flores(
            name=name,
            valor=valor,
            descripcion=descripcion,
            stock=stock,
            imagen=imagen
        )
        flor.save() #graba el objeto e bdd
        #dispositivos = FCMDevice.objects.filter(active=True)
        #dispositivos.send_message(
        #    title="Flor agregada : ",
        #    body="Se ha agregado: ",
        #    icon="/static/core/img/flor1.jpg"
        #)
        return render(request,'core/formulario.html',{'msg':'grabo','sw':True})
    return render(request,'core/formulario.html')#pasan los datos a la web

class FlorViewSet(viewsets.ModelViewSet):
    queryset = Flores.objects.all()
    serializer_class = FlorSerializer