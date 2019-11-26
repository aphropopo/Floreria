from django.shortcuts import render

# Create your views here. Crea los controladores
#Para las paginas webs
def home(request):
    return render(request,'core/index.html') 
    #Retorna la pagina renderizada

def galeria(request):
    return render(request, 'core/galeria.html')
    #Retorna la pagina renderizada

def formulario(request):
    return render(request, 'core/formulario.html')
    #Retorna la pagina renderizada

def contactanos(request):
    return render(request, 'core/contactanos.html')
    #Retorna la pagina renderizada

def carro(request):
    return render(request, 'core/carro.html')
    #Retorna la pagina renderizada