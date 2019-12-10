from django.shortcuts import render
from django.contrib.auth.models import User
# importar el sistema de autentificacion
from .models import Flores,Usuario
from django.contrib.auth import authenticate,logout,login as auth_login
# importar los "decorators" que permiten evitar el ingreso a una pagina
# sin estar logeado
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here. Crea los controladores
#Para las paginas webs
@login_required(login_url='/login/')
def home(request):
    return render(request,'core/index.html') 
    #Retorna la pagina renderizada

def login(request):
    return render(request,'core/login.html')

def login_iniciar(request):
    if request.POST:
        u=request.POST.get("txtUsuario")
        p=request.POST.get("txtPass")
        usu=authenticate(request,username=u,password=p)
        if usu is not None and usu.is_active:
            auth_login(request, usu)
            return render(request,'core/index.html')
    return render(request,'core/login.html')

@login_required(login_url='/login/')
def galeria(request):
    floress=Flores.objects.all()
    return render(request, 'core/galeria.html',{'listaflores':floress})
    #Retorna la pagina renderizada


@login_required(login_url='/login/')
def contactanos(request):
    return render(request, 'core/contactanos.html')
    #Retorna la pagina renderizada

@login_required(login_url='/login/')
def carro(request):
    return render(request, 'core/carro.html')
    #Retorna la pagina renderizada

def cerrar_sesion(request):
    logout(request)
    return render(request,'core/cerrar_sesion.html')


def registro(request):
    return render(request, 'core/registro.html')
    #Retorna la pagina renderizada

@login_required(login_url='/login/')
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
        return render(request,'core/formulario.html',{'msg':'grabo','sw':True})
    return render(request,'core/formulario.html')#pasan los datos a la web
